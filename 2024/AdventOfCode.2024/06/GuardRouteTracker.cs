using AdventOfCode._2024.Library;

namespace AdventOfCode._2024._06
{
    internal class GuardRouteTracker(string dataFilename, Part part) : APuzzle(dataFilename, part)
    {
        public override string GetAnswer()
        {
            bool[][] map;
            Guard guard;
            bool leftMap = false;
            switch (Part)
            {
                case Part.One:
                    map = GetMap(out guard);
                    while (!leftMap)
                    {
                        guard.Move(map, out leftMap, out _);
                    }

                    return guard.CountDistinctPositions().ToString();

                case Part.Two:
                    int loopObjectCount = 0;
                    map = GetMap(out guard);
                    (int X, int Y) initialPosition = guard.Position;
                    Direction initialFacing = guard.Facing;
                    for (int i = 0; i < map.Length; i++)
                    {
                        for (int j = 0; j < map[i].Length; j++)
                        {
                            guard = new Guard(initialPosition, initialFacing);
                            if (map[i][j])
                            {
                                // Already an obstacle here
                                continue;
                            }

                            map[i][j] = true;
                            leftMap = false;
                            bool looped = false;
                            while (!leftMap && !looped)
                            {
                                guard.Move(map, out leftMap, out looped);
                            }

                            if (looped)
                            {
                                loopObjectCount++;
                            }

                            map[i][j] = false;

                            Console.SetCursorPosition(0, Console.CursorTop);
                            Console.Write($"{((j + 1 + ((i + 1) * map[i].Length) * 100)) / (map.Length * map[i].Length)}% tested...          ");
                        }
                    }
                    Console.WriteLine();
                    return loopObjectCount.ToString();

                default:
                    throw new NotSupportedException();
            }
        }

        private bool[][] GetMap(out Guard guard)
        {
            string[] lines = File.ReadAllLines(DataFilename);

            guard = GetGuard(lines);
            return lines.Select(x => x.Select(y => y == '#').ToArray()).ToArray();
        }

        private static Guard GetGuard(string[] lines)
        {
            for (int i = 0; i < lines.Length; i++)
            {
                for (int j = 0; j < lines[i].Length; j++)
                {
                    switch (lines[i][j])
                    {
                        case '^':
                            return new Guard((j, i), Direction.Up);
                        case '>':
                            return new Guard((j, i), Direction.Right);
                        case 'v':
                            return new Guard((j, i), Direction.Down);
                        case '<':
                            return new Guard((j, i), Direction.Left);
                    }
                }
            }

            throw new ArgumentException("Guard not found in map");
        }

        private class Guard
        {
            private readonly Dictionary<(int, int), Direction> _visited;

            public Guard((int X, int Y) initialPosition, Direction initialFacing)
            {
                Position = initialPosition;
                Facing = initialFacing;
                _visited = new() { { Position, Facing } };
            }

            public (int X, int Y) Position { get; private set; }

            public Direction Facing { get; private set; }

            public int CountDistinctPositions()
            {
                return _visited.Count;
            }

            public void Move(bool[][] map, out bool leftMap, out bool looped)
            {
                looped = false;
                (int X, int Y) destination = Facing switch
                {
                    Direction.Up => (Position.X, Position.Y - 1),
                    Direction.Right => (Position.X + 1, Position.Y),
                    Direction.Down => (Position.X, Position.Y + 1),
                    Direction.Left => (Position.X - 1, Position.Y),
                    _ => throw new NotSupportedException(),
                };

                leftMap = destination.Y < 0 || destination.Y >= map.Length || destination.X < 0 || destination.X >= map[destination.Y].Length;
                if (leftMap)
                {
                    return;
                }

                if (map[destination.Y][destination.X])
                {
                    Turn();
                }
                else
                {
                    Position = destination;
                    if (_visited.TryGetValue(Position, out Direction previousFacing) && previousFacing == Facing)
                    {
                        looped = true;
                        return;
                    }

                    _visited[Position] = Facing;
                }
            }

            private void Turn()
            {
                Facing = (Direction)(((int)Facing + 1) % 4);
            }
        }


        private enum Direction
        {
            Up = 0,
            Right = 1,
            Down = 2,
            Left = 3
        }
    }
}