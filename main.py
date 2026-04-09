from app import play


def main():
    play.init()

    try:
        play.run()
    except KeyboardInterrupt:
        play.end()


if __name__ == "__main__":
    main()
