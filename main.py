from time import sleep
from app import play, model


def main():
    play.init()
    model.init()

    try:
        play.run()
    except KeyboardInterrupt:
        play.end()


if __name__ == "__main__":
    main()