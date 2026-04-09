from app import play


def main():
    play.init()

    try:
        play.run()
    except KeyboardInterrupt:
        play.end()
    except ConnectionError:
        play.end("Please initiate wizardlm2 by running \'ollama run wizardlm2\' within your terminal")
    except ResponseError:()
        play.end("Please install wizardlm2 by running \'ollama pull wizardlm2\' within your terminal")


if __name__ == "__main__":
    main()