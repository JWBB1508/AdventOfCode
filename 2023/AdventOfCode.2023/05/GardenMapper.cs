using AdventOfCode._2023.Library;
using System.Text.RegularExpressions;

namespace AdventOfCode._2023._05
{
    internal class GardenMapper : APuzzle
    {
        public GardenMapper(string dataFilename, Part part)
            : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            IEnumerable<string> lines = File.ReadLines(DataFilename);
            IEnumerable<Map> allMaps = lines
                            .Skip(2)
                            .Split(string.IsNullOrEmpty)
                            .Select(Map.FromData);

            long[] inputSeeds = Regex.Match(lines.First(), @"seeds: ([\d\s]+)").Groups[1].Value
                .Split(
                    (char[]?)null,
                    StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select(long.Parse)
                .ToArray();

            switch (Part)
            {
                case Part.One:
                    {
                        long minLocation = long.MaxValue;
                        foreach (long seed in inputSeeds)
                        {
                            long location = PerformMapping(
                                "seed",
                                "location",
                                seed,
                                allMaps.GroupBy(x => x.SourceType),
                                new HashSet<string>());
                            if (location < minLocation)
                            {
                                minLocation = location;
                            }
                        }

                        return minLocation.ToString();
                    }
                case Part.Two:
                    {
                        IList<(long, long)> seedRanges = new List<(long, long)>();
                        for (int i = 0; i < inputSeeds.Length; i += 2)
                        {
                            seedRanges.Add((inputSeeds[i], inputSeeds[i + 1]));
                        }
                        long location = 0;
                        while (true)
                        {
                            long seed = PerformReverseMapping(
                                "location",
                                "seed",
                                location,
                                allMaps.GroupBy(x => x.DestinationType),
                                new HashSet<string>());
                            foreach ((long MinSeed, long RangeSize) seedRange in seedRanges)
                            {
                                if (seed >= seedRange.MinSeed && seed < seedRange.MinSeed + seedRange.RangeSize)
                                {
                                    return location.ToString();
                                }
                            }

                            location++;
                        }
                    }
                default:
                    throw new InvalidOperationException($"Unknown Part: {Part}");
            }
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

        private long PerformReverseMapping(
        string destinationType,
        string sourceType,
        long value,
        IEnumerable<IGrouping<string, Map>> mapsByDestinationType,
        ISet<string> checkedTypes)
        {
            if (checkedTypes.Contains(destinationType))
            {
                throw new Exception("Infinite loop detected");
            }

            checkedTypes.Add(destinationType);

            while (destinationType != sourceType)
            {
                IEnumerable<Map> maps = mapsByDestinationType.First(x => x.Key == destinationType);
                foreach (Map map in maps)
                {
                    return PerformReverseMapping(
                        map.SourceType,
                        sourceType,
                        map.GetSourceValue(value),
                        mapsByDestinationType,
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

            public long GetSourceValue(long destinationValue)
            {
                foreach (Range range in _ranges)
                {
                    if (destinationValue >= range.MinDestinationValue
                        && destinationValue < range.MinDestinationValue + range.RangeSize)
                    {
                        return range.MinSourceValue + destinationValue - range.MinDestinationValue;
                    }
                }

                return destinationValue;
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