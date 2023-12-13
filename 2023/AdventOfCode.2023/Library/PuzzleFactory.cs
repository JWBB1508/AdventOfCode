using AdventOfCode._2023._01;
using AdventOfCode._2023._02;
using AdventOfCode._2023._03;
using AdventOfCode._2023._04;
using AdventOfCode._2023._05;
using AdventOfCode._2023._06;

namespace AdventOfCode._2023.Library
{
    internal static class PuzzleFactory
    {
        public static APuzzle GetPuzzle(short day, string dataFilename, Part part)
        {
            return day switch
            {
                1 => new TrebuchetCalibration(dataFilename, part),
                2 => new CubeGame(dataFilename, part),
                3 => new EngineSchematic(dataFilename, part),
                4 => new ScratchcardResolver(dataFilename, part),
                5 => new GardenMapper(dataFilename, part),
                6 => new BoatRacer(dataFilename, part),
                _ => throw new ArgumentOutOfRangeException(nameof(day), day, $"Day {day} not supported by PuzzleFactory"),
            };
        }
    }
}