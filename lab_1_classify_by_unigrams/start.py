"""
Language detection starter
"""
# pylint:disable=too-many-locals, unused-argument, unused-variable

import lab_1_classify_by_unigrams.main as func


def main() -> None:
    """
    Launches an implementation
    """
    with open("assets/texts/en.txt", "r", encoding="utf-8") as file_to_read_en:
        en_text = file_to_read_en.read()
    with open("assets/texts/de.txt", "r", encoding="utf-8") as file_to_read_de:
        de_text = file_to_read_de.read()
    with open("assets/texts/unknown.txt", "r", encoding="utf-8") as file_to_read_unk:
        unknown_text = file_to_read_unk.read()

    en_profile = func.create_language_profile('en', en_text)
    de_profile = func.create_language_profile('de', de_text)
    unknown_profile = func.create_language_profile('unknown', unknown_text)

    if not (isinstance(en_profile, dict) and
            isinstance(unknown_profile, dict) and
            isinstance(de_profile, dict)):
        return None

    result = func.detect_language(unknown_profile, de_profile, en_profile)
    assert result, "Detection result is None"

    return result


if __name__ == "__main__":
    main()

    print(main())
