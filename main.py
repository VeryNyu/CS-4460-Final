from app import play, model


def main():
    play.init()
    model.init()

    try:
        play.run()
    except KeyboardInterrupt:
        play.end()
    except ConnectionError:
        play.end("Please")


if __name__ == "__main__":
    main()