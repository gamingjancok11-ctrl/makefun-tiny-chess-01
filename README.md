# Tiny Chess

A chess engine in under 4 KB of Python (main.py, 4,081 bytes) for the
make.fun tiny-chess-01 bounty. Original code, written for this competition;
not a fork of sunfish or any other engine.

## Design

- 0x88 board, pseudo-legal move generation with legality filtering.
- Negamax alpha-beta with iterative deepening to a fixed budget of 30,000
  nodes per depth (never a clock, so every trial replays identically).
- Quiescence over captures and promotions, plus full replies while in check.
- Transposition table (best move, for ordering), MVV-LVA capture ordering.
- Evaluation: material plus formula piece-square terms (centrality and pawn
  advance), a bishop-pair bonus, and a king table that switches from a
  middlegame shelter table to an endgame centralisation table by phase.

## Run

The engine plays the make.fun gauntlet through the env:

    MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 -P -s main.py

It reads each position from the env, picks from the env's own legal moves,
and exits when the trial is done. Python 3.13 standard library only; no
model calls, no network except the env.

## Test

Move generation passes perft on the standard suite (start, Kiwipete,
positions 3-6) through depth 4. Local speed is about 20-25k nodes/s in
CPython, roughly 2-3 s per move in the middlegame, well inside the 10 s
move limit.

## Local trial

Against the kit's own env on practice/trial-0 (6 games, deterministic):
3 wins (depth-2, depth-3, depth-4, all by checkmate) and 3 losses
(nodes-100k, nodes-250k, nodes-500k), for a practice Elo of about 1,279
— above the 1,154 floor for the final. A 50,000-node budget was tried
and scored worse on this instance (1W 2D 3L), so the entry keeps 30,000.
