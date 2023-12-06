namespace AdventOfCode._2023.Library
{
    internal abstract class APuzzle
    {
        protected string DataFilename { get; }

        protected Part Part { get; }

        public abstract string GetAnswer();

        internal APuzzle(string dataFilename, Part part)
        {
            DataFilename = dataFilename;
            Part = part;
        }
    }
}
