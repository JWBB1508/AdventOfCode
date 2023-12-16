using AdventOfCode._2023.Library;

namespace AdventOfCode._2023._09
{
    internal class OasisExtrapolator : APuzzle
    {
        public OasisExtrapolator(string dataFilename, Part part) : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            return File.ReadAllLines(DataFilename)
                .Select(Sequence.FromData)
                .Sum(x => Part == Part.Two ? x.ExtrapolateBackwards() : x.ExtrapolateForwards())
                .ToString();
        }

        private class Sequence
        {
            private readonly long[] _values;
            private readonly Sequence? _child;

            private Sequence(long[] values, Sequence? child)
            {
                _values = values;
                _child = child;
            }

            public long First => _values.First();

            public long Last => _values.Last();

            public bool IsFinal => _child == null;

            public static Sequence FromData(string data)
            {
                long[] values = data
                    .Split((char[]?)null, StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries)
                    .Select(long.Parse)
                    .ToArray();

                return new Sequence(values, GetChild(values));
            }

            public long ExtrapolateForwards()
            {
                return Last + (_child == null ? 0 : _child.ExtrapolateForwards());
            }

            public long ExtrapolateBackwards()
            {
                return First - (_child == null ? 0 : _child.ExtrapolateBackwards());
            }

            private static Sequence GetChild(long[] values)
            {
                IList<long> list = new List<long>();
                for (var i = 0; i < values.Length - 1; i++)
                {
                    list.Add(values[i + 1] - values[i]);
                }

                long[] childValues = list.ToArray();
                return new Sequence(childValues, childValues.All(x => x == 0) ? null : GetChild(childValues));
            }
        }
    }
}
