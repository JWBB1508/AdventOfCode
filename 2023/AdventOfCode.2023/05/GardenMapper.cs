using AdventOfCode._2023.Library;
using System.Text.RegularExpressions;

namespace AdventOfCode._2023._05
{
    internal class GardenMapper : APuzzle
    {
        public GardenMapper(string dataFilename, Part part) : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            IEnumerable<string> lines = File.ReadLines(DataFilename);
            IEnumerable<long> seeds = Regex.Match(lines.First(), @"seeds: ([\d\s]+)").Groups[1].Value.Split(
                            (char[]?)null,
                            StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select(long.Parse);

            IEnumerable<IGrouping<string, Map>> mapsBySourceType = lines
                .Skip(2)
                .Split(string.IsNullOrEmpty)
                .Select(Map.FromData)
                .GroupBy(x => x.SourceType);

            long minLocation = long.MaxValue;
            foreach (long seed in seeds)
            {
                long location = PerformMapping("seed", "location", seed, mapsBySourceType, new HashSet<string>());
                if (location < minLocation)
                {
                    minLocation = location;
                }
            }

            return minLocation.ToString();
        }

        private long PerformMapping(
            string sourceType,
            string destinationType,
            long value,
            IEnumerable<IGrouping<string, Map>> mapsBySourceType,
            ISet<string> checkedTypes)
        {
            if (checkedTypes.Contains(sourceType))
            {
                throw new Exception("Infinite loop detected");
            }

            checkedTypes.Add(sourceType);

            while (sourceType != destinationType)
            {
                IEnumerable<Map> maps = mapsBySourceType.First(x => x.Key == sourceType);
                foreach (Map map in maps)
                {
                    return PerformMapping(
                        map.DestinationType,
                        destinationType,
                        map.GetDestinationValue(value),
                        mapsBySourceType,
                        checkedTypes);
                }
            }

            return value;
        }

        private class Map
        {
            private readonly Range[] _ranges;

            private Map(string sourceType, string destinationType, Range[] ranges)
            {
                _ranges = ranges;

                SourceType = sourceType;
                DestinationType = destinationType;
            }

            public string SourceType { get; }

            public string DestinationType { get; }

            public static Map FromData(IEnumerable<string> lines)
            {
                Match labelMatch = Regex.Match(lines.First(), @"(\w+)-to-(\w+) map:");

                Range[] ranges = lines
                    .Skip(1)
                    .Select(x => x
                        .Split(
                            (char[]?)null,
                            StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                        .Select(long.Parse)
                        .ToArray())
                    .Select(x => new Range(x[1], x[0], x[2]))
                    .ToArray();

                return new Map(labelMatch.Groups[1].Value, labelMatch.Groups[2].Value, ranges);
            }

            public long GetDestinationValue(long sourceValue)
            {
                foreach (Range range in _ranges)
                {
                    if (sourceValue >= range.MinSourceValue
                        && sourceValue < range.MinSourceValue + range.RangeSize)
                    {
                        return range.MinDestinationValue + sourceValue - range.MinSourceValue;
                    }
                }

                return sourceValue;
            }

            private class Range
            {
                public long MinSourceValue { get; }

                public long MinDestinationValue { get; }

                public long RangeSize { get; }

                public Range(long minSourceValue, long minDestinationValue, long rangeSize)
                {
                    MinSourceValue = minSourceValue;
                    MinDestinationValue = minDestinationValue;
                    RangeSize = rangeSize;
                }
            }
        }
    }
}
