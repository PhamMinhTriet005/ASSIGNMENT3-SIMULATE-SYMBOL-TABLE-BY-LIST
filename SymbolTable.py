from StaticError import *
from Symbol import *
from functools import *

def create_symbol(name, typ):
    """Create a symbol with the given name and type."""
    return Symbol(name, typ)

def create_scope(symbols=None, level=0):
    """Create a new scope with the given symbols and level."""
    return {
        "symbols": symbols or [],
        "level": level
    }

def add_symbol(scope, symbol):
    """Add a symbol to the given scope."""
    return {
        "symbols": scope["symbols"] + [symbol],
        "level": scope["level"]
    }

def create_symbol_table(scopes=None):
    """Create a new symbol table with the given scopes."""
    return scopes or [create_scope()]

def get_current_scope(symbol_table):
    """Get the current scope from the symbol table."""
    return symbol_table[-1]

def check_redeclared(scope, name):
    """Check if a symbol with the given name is already declared in the scope."""
    matching = list(filter(lambda symbol: symbol.name == name, scope["symbols"]))
    return len(matching) > 0

def insert_symbol(symbol_table, name, typ):
    """Insert a symbol into the current scope of the symbol table."""
    current_scope = get_current_scope(symbol_table)
    
    if check_redeclared(current_scope, name):
        raise Redeclared(f"INSERT {name} {typ}")
    
    new_symbol = create_symbol(name, typ)
    new_scope = add_symbol(current_scope, new_symbol)
    
    return symbol_table[:-1] + [new_scope]

def lookup_symbol(symbol_table, name):
    """Look up a symbol in the symbol table, from current scope to global scope."""
    def find_in_scope(acc, scope):
        if acc is not None:
            return acc
        matching = list(filter(lambda symbol: symbol.name == name, scope["symbols"]))
        if matching:
            return scope["level"]
        return None
    
    result = reduce(find_in_scope, reversed(symbol_table), None)
    if result is None:
        raise Undeclared(f"LOOKUP {name}")
    return result

def find_symbol(symbol_table, name):
    """Find a symbol in the symbol table, from current scope to global scope."""
    def find_in_scope(acc, scope):
        if acc is not None:
            return acc
        matching = list(filter(lambda symbol: symbol.name == name, scope["symbols"]))
        if matching:
            return matching[0]
        return None
    
    result = reduce(find_in_scope, reversed(symbol_table), None)
    if result is None:
        raise Undeclared(f"LOOKUP {name}")
    return result

def begin_block(symbol_table):
    """Begin a new block (scope) in the symbol table."""
    current_level = get_current_scope(symbol_table)["level"]
    new_scope = create_scope(level=current_level + 1)
    return symbol_table + [new_scope]

def end_block(symbol_table):
    """End the current block (scope) in the symbol table."""
    if len(symbol_table) <= 1:
        raise UnknownBlock()
    return symbol_table[:-1]

def check_type_match(symbol_table, name, value):
    """Check if the type of the value matches the type of the symbol."""
    # Try to find the symbol in the table
    target_symbol = find_symbol(symbol_table, name)
    
    # If value is a number
    if value.isdigit():
        return target_symbol.typ == "number"
    
    # If value starts with an apostrophe (potential string)
    if value.startswith("'"):
        # Check if it's a properly formatted string (starts and ends with apostrophe)
        if len(value) < 2 or value[-1] != "'":
            raise InvalidInstruction(f"ASSIGN {name} {value}")
            
        # Check if string content is valid (only alphanumeric characters)
        content = value[1:-1]
        if not all(c.isalnum() for c in content):
            raise InvalidInstruction(f"ASSIGN {name} {value}")
        return target_symbol.typ == "string"
    
    # If value is another identifier, validate it first
    if not validate_identifier(value):
        raise InvalidInstruction(f"ASSIGN {name} {value}")
    
    # If it's a valid identifier, look it up in the symbol table
    try:
        source_symbol = find_symbol(symbol_table, value)
        return target_symbol.typ == source_symbol.typ
    except:
        raise Undeclared(f"ASSIGN {name} {value}")

def validate_identifier(name):
    """Validate that the identifier name follows the required format."""
    # Must start with lowercase letter
    if not name or not name[0].islower():
        return False
    
    # Must only contain lowercase letters, uppercase letters, digits, and underscores
    return all(c.islower() or c.isupper() or c.isdigit() or c == '_' for c in name)

def get_printable_symbols(symbol_table):
    """Get all visible symbols in the symbol table, formatted for printing."""
    # We'll track insertion order in our collection logic
    def collect_symbols(state, scope):
        counter, acc = state
        
        def add_symbol(state, symbol):
            inner_counter, inner_acc = state
            if symbol.name not in inner_acc:
                # Store (level, insertion_counter) for each symbol
                inner_acc[symbol.name] = (scope["level"], inner_counter)
                inner_counter += 1
            return (inner_counter, inner_acc)
        
        new_counter, new_acc = reduce(add_symbol, scope["symbols"], (counter, acc))
        return (new_counter, new_acc)
    
    # Start with counter at 0 and empty dict
    _, visible_symbols = reduce(collect_symbols, reversed(symbol_table), (0, {}))
    
    # Convert to list of (name, level, insertion_order) tuples
    pairs = list(map(lambda item: (item[0], item[1][0], item[1][1]), visible_symbols.items()))
    
    # Sort using insertion order as secondary criterion after level
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        
        mid = len(lst) // 2
        left_half = merge_sort(lst[:mid])
        right_half = merge_sort(lst[mid:])
        
        def merge(left, right, acc=None):
            acc = acc or []
            
            if not left:
                return acc + right
            
            if not right:
                return acc + left
            
            # Sort by level first, then by insertion order
            if left[0][1] < right[0][1] or (left[0][1] == right[0][1] and left[0][2] < right[0][2]):
                return merge(left[1:], right, acc + [left[0]])
            else:
                return merge(left, right[1:], acc + [right[0]])
        
        return merge(left_half, right_half)
    
    sorted_result = merge_sort(pairs)
    
    # Format as "name//level" using map
    formatted_result = list(map(lambda x: f"{x[0]}//{x[1]}", sorted_result))
    
    return formatted_result

def process_command(command, symbol_table):
    """Process a single command and update the symbol table accordingly."""
    # Check for completely empty command
    if not command.strip():
        raise InvalidInstruction("Invalid command")
     # Check for leading spaces - use generic message
    if command.startswith(" "):
        raise InvalidInstruction("Invalid command")

    # For all formatting issues, use the actual command in the error message
    if command != command.strip() or "  " in command:
        raise InvalidInstruction(command)
        
    parts = command.split()
    
    if not parts:
        raise InvalidInstruction("Invalid command")  # Shouldn't reach here, but just in case
    
    command_type = parts[0]
    
    # Check if command_type is a valid command name (exact match required)
    valid_commands = ["INSERT", "ASSIGN", "BEGIN", "END", "LOOKUP", "PRINT", "RPRINT"]
    if command_type not in valid_commands:
        raise InvalidInstruction("Invalid command")
    
    if command_type == "INSERT":
        if len(parts) != 3:
            raise InvalidInstruction(command)
        
        name, typ = parts[1], parts[2]
        
        # Validate identifier name
        if not validate_identifier(name):
            raise InvalidInstruction(command)
        
        # Validate type (must be 'number' or 'string')
        if typ not in ["number", "string"]:
            raise InvalidInstruction(command)
        
        return insert_symbol(symbol_table, name, typ), "success"
    
    elif command_type == "ASSIGN":
        if len(parts) != 3:
            raise InvalidInstruction(command)
        
        name, value = parts[1], parts[2]
        
        # First validate identifier format
        if not validate_identifier(name):
            raise InvalidInstruction(command)
        
        # Then check if it exists in symbol table
        try:
            target_symbol = find_symbol(symbol_table, name)
        except:
            raise Undeclared(command)
        
        # Check if type matches
        if not check_type_match(symbol_table, name, value):
            raise TypeMismatch(command)
        
        return symbol_table, "success"
    
    elif command_type == "BEGIN":
        if len(parts) != 1:
            raise InvalidInstruction(command)
        
        return begin_block(symbol_table), None
    
    elif command_type == "END":
        if len(parts) != 1:
            raise InvalidInstruction(command)
        
        return end_block(symbol_table), None
    
    elif command_type == "LOOKUP":
        if len(parts) != 2:
            raise InvalidInstruction(command)
        
        name = parts[1]
        if not validate_identifier(name):
            raise InvalidInstruction(command)
        level = lookup_symbol(symbol_table, name)
        
        return symbol_table, str(level)
    
    elif command_type == "PRINT":
        if len(parts) != 1:
            raise InvalidInstruction(command)
        
        return symbol_table, (" ".join(get_printable_symbols(symbol_table)) 
                             if get_printable_symbols(symbol_table) else "")
    
    elif command_type == "RPRINT":
        if len(parts) != 1:
            raise InvalidInstruction(command)
        
        # For RPRINT, we reverse the order of the symbols
        symbols = get_printable_symbols(symbol_table)
        return symbol_table, (" ".join(list(reversed(symbols))) 
                             if symbols else "")
    
    else:
        raise InvalidInstruction("Invalid command")

def simulate(list_of_commands):
    """
    Executes a list of commands and processes them sequentially.

    Args:
        list_of_commands (list[str]): A list of commands to be executed.

    Returns:
        list[str]: A list of return messages corresponding to each command.
    """
    def process_commands_recursive(cmds, st, results):
        # Base case: all commands processed
        if not cmds:
            # Check for unclosed blocks
            if len(st) > 1:
                raise UnclosedBlock(get_current_scope(st)["level"])
            return results
        
        # Process the next command
        cmd = cmds[0]
        try:
            new_st, result = process_command(cmd, st)
            new_results = results + [result] if result is not None else results
            return process_commands_recursive(cmds[1:], new_st, new_results)
        except StaticError as e:
            return [str(e)]
    
    try:
        return process_commands_recursive(list_of_commands, create_symbol_table(), [])
    except StaticError as e:
        return [str(e)]