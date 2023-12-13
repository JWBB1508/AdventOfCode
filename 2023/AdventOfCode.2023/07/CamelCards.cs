using AdventOfCode._2023.Library;

namespace AdventOfCode._2023._07
{
    internal class CamelCards : APuzzle
    {
        public CamelCards(string dataFilename, Part part) : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            Hand[] hands = File
                .ReadAllLines(DataFilename)
                .Select(x => Hand.FromData(x, Part))
                .OrderBy(x => x)
                .ToArray();

            long totalWinnings = 0;
            for (int i = 0; i < hands.Length; i++)
            {
                totalWinnings += hands[i].Bid * (i + 1);
            }

            return totalWinnings.ToString();
        }

        private class Hand : IComparable
        {
            private readonly Card[] _cards;

            private Hand(Card[] cards, int bid)
            {
                if (cards.Length != 5)
                {
                    throw new ArgumentException($"Unexpected hand size: {cards.Length}", nameof(cards));
                }

                _cards = cards;

                Bid = bid;
            }

            public int Bid { get; }

            public static Hand FromData(string line, Part part)
            {
                string[] parts = line
                    .Split((char[]?)null, StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);

                return new Hand(parts[0].Select(x => GetCard(x, part)).ToArray(), int.Parse(parts[1]));
            }

            public int CompareTo(object? obj)
            {
                if (obj is not Hand hand)
                {
                    throw new ArgumentException("Cannot compare to an object that is not a Hand", nameof(obj));
                }

                if (GetHandType() > hand.GetHandType())
                {
                    return 1;
                }

                if (GetHandType() < hand.GetHandType())
                {
                    return -1;
                }

                for (int i = 0; i < _cards.Length; i++)
                {
                    if (_cards[i] > hand._cards[i])
                    {
                        return 1;
                    }

                    if (_cards[i] < hand._cards[i])
                    {
                        return -1;
                    }
                }

                return 0;
            }

            private HandType GetHandType()
            {
                IGrouping<Card, Card>[] groupedCards = GetBestHandUsingJokers().GroupBy(x => x).ToArray();
                return groupedCards.Length switch
                {
                    1 => HandType.FiveOfAKind,
                    2 => groupedCards.Max(x => x.Count()) switch
                    {
                        4 => HandType.FourOfAKind,
                        3 => HandType.FullHouse,
                        _ => throw new InvalidOperationException("Impossible!"),
                    },
                    3 => groupedCards.Max(x => x.Count()) switch
                    {
                        3 => HandType.ThreeOfAKind,
                        2 => HandType.TwoPair,
                        _ => throw new InvalidOperationException("Impossible!"),
                    },
                    4 => HandType.Pair,
                    5 => HandType.HighCard,
                    _ => throw new InvalidOperationException("Impossible!"),
                };
            }

            private Card[] GetBestHandUsingJokers()
            {
                if (!_cards.Any(x => x == Card.Joker))
                {
                    return _cards;
                }

                IGrouping<Card, Card>[] groupedCards = _cards.GroupBy(x => x).ToArray();
                Card? bestCard = groupedCards
                    .Where(x => x.Key != Card.Joker)
                    .OrderByDescending(x => x.Count())
                    .FirstOrDefault()
                    ?.Key;

                if (!bestCard.HasValue)
                {
                    bestCard = Card.Ace;
                }

                Card[] bestHand = (Card[])_cards.Clone();
                for (int i = 0; i < bestHand.Length; i++)
                {
                    if (bestHand[i] == Card.Joker)
                    {
                        bestHand[i] = bestCard.Value;
                    }
                }

                return bestHand;
            }

            private static Card GetCard(char card, Part part)
            {
                return card switch
                {
                    '2' => Card.Two,
                    '3' => Card.Three,
                    '4' => Card.Four,
                    '5' => Card.Five,
                    '6' => Card.Six,
                    '7' => Card.Seven,
                    '8' => Card.Eight,
                    '9' => Card.Nine,
                    'T' => Card.Ten,
                    'J' => part == Part.Two ? Card.Joker : Card.Jack,
                    'Q' => Card.Queen,
                    'K' => Card.King,
                    'A' => Card.Ace,
                    _ => throw new ArgumentOutOfRangeException(nameof(card), card, "Unrecognised card"),
                };
            }

            public enum HandType
            {
                HighCard = 0,
                Pair = 1,
                TwoPair = 2,
                ThreeOfAKind = 3,
                FullHouse = 4,
                FourOfAKind = 5,
                FiveOfAKind = 6
            }

            private enum Card
            {
                Joker = -1,
                Two = 0,
                Three = 1,
                Four = 2,
                Five = 3,
                Six = 4,
                Seven = 5,
                Eight = 6,
                Nine = 7,
                Ten = 8,
                Jack = 9,
                Queen = 10,
                King = 11,
                Ace = 12
            }
        }
    }
}
