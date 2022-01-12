from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # 2. Test the plural determiners.
    plural_determiners = ["some", "many"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    singular_nouns = ["adult", "bird", "boy", "car", "cat",
                      "child", "dog", "girl", "man", "woman"]

    for _ in range(4):
        word = get_noun(1)
        assert word in singular_nouns

    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
                    "children", "dogs", "girls", "men", "women"]

    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns


def test_get_verb():
    past_tense = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(1, "past")
        assert word in past_tense

    singular_present = ["drinks", "eats", "grows", "laughs", "thinks",
                        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        word = get_verb(1, "present")
        assert word in singular_present

    plural_present = ["drink", "eat", "grow", "laugh", "think",
                      "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        word = get_verb(2, "present")
        assert word in plural_present

    future_tense = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write"]

    for _ in range(4):
        word = get_verb(1, "future")
        assert word in future_tense


def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    for _ in range(4):
        word = get_preposition()
        assert word in prepositions


def test_get_prepositional_phrase():
    for _ in range(4):
        words = get_prepositional_phrase(1)
        words_split = words.split(",")
        assert len(words_split)
        # assert words_split --- also passes, but I don't know why


pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])
