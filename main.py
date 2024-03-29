from time import sleep
from json import load
import RPi.GPIO as gpio_config

import travis_API as ta


def main():
    """
    Runs the main functions, the whole program
    """
    gpio_config.setmode(gpio_config.BCM)
    with open("repo_ids.json") as repo_ids_file:
        repo_ids = load(repo_ids_file)
    with open("GPIO.json") as gpio_file:
        gpio_maps = load(gpio_file)
    for gpio_map in gpio_maps:
        for gpio_pin in gpio_map:
            gpio_config.setup(gpio_pin, gpio_config.OUT)
            gpio_config.output(gpio_pin, gpio_config.HIGH)
            sleep(0.2)
            gpio_config.output(gpio_pin, gpio_config.LOW)
    while True:
        for i in range(len(repo_ids)):
            last_build_result = ta.get_build_repo_status(repo_ids[i])
            print(repo_ids[i])
            print(last_build_result)
            if last_build_result == 0:
                gpio_config.output(gpio_maps[i][0], gpio_config.HIGH)
                gpio_config.output(gpio_maps[i][1], gpio_config.LOW)
                gpio_config.output(gpio_maps[i][2], gpio_config.LOW)
            elif last_build_result == 1:
                gpio_config.output(gpio_maps[i][0], gpio_config.LOW)
                gpio_config.output(gpio_maps[i][1], gpio_config.LOW)
                gpio_config.output(gpio_maps[i][2], gpio_config.HIGH)
            elif last_build_result is None:
                gpio_config.output(gpio_maps[i][0], gpio_config.LOW)
                gpio_config.output(gpio_maps[i][1], gpio_config.HIGH)
                gpio_config.output(gpio_maps[i][2], gpio_config.LOW)
            else:
                gpio_config.output(gpio_maps[i][0], gpio_config.LOW)
                gpio_config.output(gpio_maps[i][1], gpio_config.LOW)
                gpio_config.output(gpio_maps[i][2], gpio_config.LOW)
            sleep(1)

main()
