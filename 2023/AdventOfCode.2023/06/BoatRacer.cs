using AdventOfCode._2023.Library;

namespace AdventOfCode._2023._06
{
    internal class BoatRacer : APuzzle
    {
        public BoatRacer(string dataFilename, Part part) : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            string[] lines = File.ReadAllLines(DataFilename);

            long[] times = lines[0]
                .Split((char[]?)null, StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries)
                .Skip(1)
                .Select(long.Parse)
                .ToArray();

            if (Part == Part.Two)
            {
                times = new[] { long.Parse(string.Join(string.Empty, times)) };
            }

            long[] records = lines[1]
                .Split((char[]?)null, StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries)
                .Skip(1)
                .Select(long.Parse)
                .ToArray();

            if (Part == Part.Two)
            {
                records = new[] { long.Parse(string.Join(string.Empty, records)) };
            }

            long product = 1;
            for (long i = 0; i < times.Length; i++)
            {
                long time = times[i];
                long record = records[i];

                long victories = 0;

                for (long hold = 1; hold < time; hold++)
                {
                    long distance = (time - hold) * hold;
                    if (distance > record)
                    {
                        victories++;
                    }
                }

                product *= victories;
            }

            return product.ToString();
        }
    }
}
