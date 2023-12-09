using AdventOfCode._2023.Library;

namespace AdventOfCode._2023._03
{
    internal class EngineSchematic : APuzzle
    {
        public EngineSchematic(string dataFilename, Part part) : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            IEnumerable<PartLabel> partLabels = Schematic.FromData(File.ReadAllLines(DataFilename)).GetPartLabels();

            switch (Part)
            {
                case Part.One:
                    return partLabels
                        .GroupBy(x => (x.PartNumberY, x.PartNumberX))
                        .Sum(x => x.First().PartNumber)
                        .ToString();

                case Part.Two:
                    {
                        return partLabels
                            .GroupBy(x => (x.SymbolY, x.SymbolX))
                            .Where(x => x.First().Symbol == '*')
                            .Where(x => x.Count() == 2)
                            .Sum(x => x.Aggregate(1, (product, symbol) => product * symbol.PartNumber))
                            .ToString();
                    }

                default:
                    throw new InvalidOperationException($"Unknown Part: {Part}");
            }
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

            public IEnumerable<PartLabel> GetPartLabels()
            {
                IList<PartLabel> partLabels = new List<PartLabel>();

                var y = 0;
                while (y < _schematic.Length)
                {
                    var x = 0;
                    while (x < _schematic[y].Length)
                    {
                        string partNumber = string.Empty;
                        ISet<(int Y, int X, char Symbol)> symbols = new HashSet<(int, int, char)>();
                        while (x < _schematic[y].Length && char.IsDigit(_schematic[y][x]))
                        {
                            symbols.UnionWith(GetAdjacentSymbols(y, x));
                            partNumber += _schematic[y][x];
                            x += 1;
                        }

                        if (!string.IsNullOrEmpty(partNumber))
                        {
                            foreach (var symbol in symbols)
                            {
                                partLabels.Add(new PartLabel(int.Parse(partNumber), y, x - partNumber.Length, symbol.Symbol, symbol.Y, symbol.X));
                            }
                        }

                        x += 1;
                    }

                    y += 1;
                }

                return partLabels;
            }

            private static bool IsSymbol(char value)
            {
                return !char.IsDigit(value) && value != '.';
            }

            private ISet<(int Y, int X, char Symbol)> GetAdjacentSymbols(int y, int x)
            {
                ISet<(int Y, int X, char Symbol)> symbols = new HashSet<(int, int, char)>();

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
                            symbols.Add((yValue, xValue, _schematic[yValue][xValue]));
                        }
                    }
                }

                return symbols;
            }
        }

        private class PartLabel
        {
            public int PartNumber { get; }

            public int PartNumberY { get; }

            public int PartNumberX { get; }

            public char Symbol { get; }

            public int SymbolY { get; }

            public int SymbolX { get; }

            public PartLabel(int partNumber, int partNumberY, int partNumberX, char symbol, int symbolY, int symbolX)
            {
                PartNumber = partNumber;
                PartNumberY = partNumberY;
                PartNumberX = partNumberX;
                Symbol = symbol;
                SymbolY = symbolY;
                SymbolX = symbolX;
            }
        }
    }
}