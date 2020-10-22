from src.pattern_matcher import get_input_setup, get_pattern_matches


def main():
    patternsList, paths = get_input_setup()
    get_pattern_matches(patternsList, paths)


if __name__ == "__main__":
    main()
