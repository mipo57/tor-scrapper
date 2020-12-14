import requests
import os
from time import sleep
import click


@click.command()
@click.option("--input_file", type=click.Path(exists=True), required=True)
@click.option("--output_file", type=click.Path(exists=False, file_okay=True), required=True)
def main(input_file: str, output_file: str):
    with open(input_file, 'r') as f:
        data = f.read()

    with open(output_file, 'w') as f:
        f.write(data + "\n")

        for i in range (3):
            result = requests.get("https://api.myip.com", proxies={'http':  'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}, timeout=15)

            # TODO: Only do if ip is blocked
            os.system("sudo killall -HUP tor")
            sleep(2)

            f.write(result.text + '\n')



if __name__ == "__main__":
    main()