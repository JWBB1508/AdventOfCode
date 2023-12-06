using AdventOfCode._2023.Library;

namespace AdventOfCode._2023._03
{
    internal class EngineSchematic : APuzzle
    {
        public EngineSchematic(string dataFilename, Part part) : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            return Schematic.FromData(File.ReadAllLines(DataFilename))
                .GetPartNumbers()
                .Sum(x => x.Number)
                .ToString();
        }
        
        private class Schematic
        {
            private readonly char[][] _schematic;

            private Schematic(char[][] schematic)
            {
                _schematic = schematic;
            }

            public static Schematic FromData(IEnumerable<string> lines)
            {
                return new Schematic(lines.Select(x => x.ToCharArray()).ToArray());
            }

            public IEnumerable<(int Number, int Y, int X)> GetPartNumbers()
            {
                IList<(int Number, int Y, int X)> partNumbers = new List<(int, int, int)>();

                var y = 0;
                while (y < _schematic.Length)
                {
                    var x = 0;
                    while (x < _schematic[y].Length)
                    {
                        string partNumber = string.Empty;
                        bool isAdjacentToPart = false;
                        while (x < _schematic[y].Length && char.IsDigit(_schematic[y][x]))
                        {
                            isAdjacentToPart = isAdjacentToPart || IsAdjacentToPart(y, x);
                            partNumber += _schematic[y][x];
                            x += 1;
                        }

                        if (!string.IsNullOrEmpty(partNumber) && isAdjacentToPart)
                        {
                            partNumbers.Add((int.Parse(partNumber), y, x - partNumber.Length));
                        }

                        x += 1;
                    }

                    y += 1;
                }

                return partNumbers;
            }

            private bool IsAdjacentToPart(int y, int x)
            {
                var yValues = new[] { y - 1, y, y + 1 };
                var xValues = new[] { x - 1, x, x + 1 };

                foreach (var yValue in yValues)
                {
                    if (yValue < 0 || yValue >= _schematic.Length)
                    {
                        continue;
                    }

                    foreach (var xValue in xValues)
                    {
                        if (xValue < 0 || xValue >= _schematic[yValue].Length)
                        {
                            continue;
                        }

                        if (IsSymbol(_schematic[yValue][xValue]))
                        {
                            return true;
                        }
                    }
                }

                return false;
            }

            private bool IsSymbol(char value)
            {
                return !char.IsDigit(value) && value != '.';
            }

            private short CountAdjacentPartNumbers(int y, int x)
            {
                var yValues = new[] { y - 1, y, y + 1 };
                var xValues = new[] { x - 1, x, x + 1 };

                var count = 0;

                foreach (var yValue in yValues)
                {
                    if (yValue < 0 || yValue >= _schematic.Length)
                    {
                        continue;
                    }

                    foreach (var xValue in xValues)
                    {
                        if (xValue < 0 || xValue >= _schematic[yValue].Length)
                        {
                            continue;
                        }

                        if (char.IsDigit(_schematic[yValue][xValue]))
                        {
                            
                        }
                    }
                }

                return count;
            }
        }
    }
}
