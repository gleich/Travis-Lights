from json import load
import RPi.GPIO as GPIO
from time import sleep

import travis_API as ta

def main():
    """
    Run main
    """
    GPIO.setmode(GPIO.BCM)
    with open("repo_ids.json") as repo_ids_json:
        repo_ids = load(repo_ids_json)
    with open("GPIO.json") as GPIO_json:
        GPIO_maps = load(GPIO_json)
    total_pin = []
    for GPIO_map in GPIO_maps:
        for GPIO in GPIO_map:
            total_pin.append(GPIO)
    for pin in total_pin:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        sleep(0.50)
        GPIO.output(pin, GPIO.LOW)
    repo_one_color = ""
    repo_two_color = ""
    repo_three_color = ""
    repo_four_color = ""
    for repo_id in repo_ids:
        for GPIO_map in GPIO_maps:
            build_status = ta.get_build_repo_status(repo_id)


main()
