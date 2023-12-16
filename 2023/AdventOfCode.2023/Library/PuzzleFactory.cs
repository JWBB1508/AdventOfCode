namespace AdventOfCode._2023.Library
{
    internal static class PuzzleFactory
    {
        public static APuzzle GetPuzzle(short day, string dataFilename, Part part)
        {
            return day switch
            {
                1 => new _01.TrebuchetCalibration(dataFilename, part),
                2 => new _02.CubeGame(dataFilename, part),
                3 => new _03.EngineSchematic(dataFilename, part),
                4 => new _04.ScratchcardResolver(dataFilename, part),
                5 => new _05.GardenMapper(dataFilename, part),
                6 => new _06.BoatRacer(dataFilename, part),
                7 => new _07.CamelCards(dataFilename, part),
                8 => new _08.NetworkNavigator(dataFilename, part),
                9 => new _09.OasisExtrapolator(dataFilename, part),
                _ => throw new ArgumentOutOfRangeException(nameof(day), day, $"Day {day} not supported by PuzzleFactory"),
            };
        }
    }
}