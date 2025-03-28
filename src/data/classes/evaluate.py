from data.classes.board import Board

PIECE_VALUES = {
    'Pawn': 1,
    'Knight': 3,
    'Bishop': 3,
    'Rook': 5,
    'Queen': 9,
    'King': 0  # King value doesn't matter for checkmate detection
}

# Evaluates current board state
def evaluate(board):
    score = 0
    for square in board.squares:
        piece = square.occupying_piece
        if piece:
            value = PIECE_VALUES.get(piece.__class__.__name__, 0)
            if piece.color == 'white':
                score += value
            else:
                score -= value
    
    # Need to implement this in the board class
    if board.is_checkmate():
        return -float('inf') if board.turn == 'white' else float('inf')
        
    return score

# Recursively calls itself to a certain depth and returns evaluation
def minimax(board, depth, alpha, beta):
    # Need to implement game over func
    if depth == 0 or board.is_game_over():
        return evaluate(board)
    # Maximizing player
    if board.turn == 'white':
        max_eval = -float('inf')
        for move in board.get_all_legal_moves():
            piece, target_square = move
            
            # Save current state
            original_pos = piece.pos
            original_has_moved = piece.has_moved
            captured_piece = target_square.occupying_piece
            original_turn = board.turn

            # Make move
            piece.move(board, target_square)
            board.turn = 'black'

            # Evaluate
            eval_score = minimax(board, depth-1, alpha, beta)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)

            # Undo move
            piece.pos = original_pos
            piece.x, piece.y = original_pos
            piece.has_moved = original_has_moved
            target_square.occupying_piece = captured_piece
            board.get_square_from_pos(original_pos).occupying_piece = piece
            board.turn = original_turn

            if beta <= alpha:
                break
        return max_eval
    else:  
        # Minimizing player
        min_eval = float('inf')
        for move in board.get_all_legal_moves():
            piece, target_square = move

            # Save current state
            original_pos = piece.pos
            original_has_moved = piece.has_moved
            captured_piece = target_square.occupying_piece
            original_turn = board.turn

            # Make move
            piece.move(board, target_square)
            board.turn = 'white'

            # Evaluate
            eval_score = minimax(board, depth-1, alpha, beta)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)

            # Undo move
            piece.pos = original_pos
            piece.x, piece.y = original_pos
            piece.has_moved = original_has_moved
            target_square.occupying_piece = captured_piece
            board.get_square_from_pos(original_pos).occupying_piece = piece
            board.turn = original_turn

            if beta <= alpha:
                break
        return min_eval

# Finds best move using minimax algo
def find_best_move(board, depth):
    best_move = None
    alpha = -float('inf')
    beta = float('inf')

    if board.turn == 'white':
        best_value = -float('inf')
        for move in board.get_all_legal_moves():
            piece, target_square = move

            # Save state
            original_pos = piece.pos
            original_has_moved = piece.has_moved
            captured_piece = target_square.occupying_piece
            original_turn = board.turn

            # Make move
            piece.move(board, target_square)
            board.turn = 'black'
            # Evaluate
            current_value = minimax(board, depth-1, alpha, beta)

            # Undo move
            piece.pos = original_pos
            piece.x, piece.y = original_pos
            piece.has_moved = original_has_moved
            target_square.occupying_piece = captured_piece
            board.get_square_from_pos(original_pos).occupying_piece = piece
            board.turn = original_turn

            if current_value > best_value:
                best_value = current_value
                best_move = move
            alpha = max(alpha, best_value)
    else:
        best_value = float('inf')
        for move in board.get_all_legal_moves():
            piece, target_square = move

            # Save state
            original_pos = piece.pos
            original_has_moved = piece.has_moved
            captured_piece = target_square.occupying_piece
            original_turn = board.turn

            # Make move
            piece.move(board, target_square)
            board.turn = 'white'
            # Evaluate
            current_value = minimax(board, depth-1, alpha, beta)

            # Undo move
            piece.pos = original_pos
            piece.x, piece.y = original_pos
            piece.has_moved = original_has_moved
            target_square.occupying_piece = captured_piece
            board.get_square_from_pos(original_pos).occupying_piece = piece
            board.turn = original_turn

            if current_value < best_value:
                best_value = current_value
                best_move = move
            beta = min(beta, best_value)

    return best_move