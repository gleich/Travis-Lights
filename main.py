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
        for GPIO_PIN in GPIO_map:
            total_pin.append(GPIO_PIN)
    for pin in total_pin:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(pin, GPIO.LOW)
    colors = ["", "", "", ""]
    repo_number = 0
    while True:
        for repo_id in repo_ids:
            for GPIO_map2 in GPIO_maps:
                repo_number += 1
                if repo_number == 4:
                    repo_number -= 4
                build_status = ta.get_build_repo_status(repo_id)
                print(build_status)
                if build_status == 0 and colors[repo_number] != "green":
                    colors[repo_number] = "green"
                    GPIO.output(GPIO_map2[0], GPIO.HIGH)
                    GPIO.output(GPIO_map2[1], GPIO.LOW)
                    GPIO.output(GPIO_map2[2], GPIO.LOW)
                elif build_status == 1 and colors[repo_number] != "red":
                    colors[repo_number] = "red"
                    GPIO.output(GPIO_map2[0], GPIO.LOW)
                    GPIO.output(GPIO_map2[1], GPIO.LOW)
                    GPIO.output(GPIO_map2[2], GPIO.HIGH)
                elif build_status == None and colors[repo_number] != "yellow":
                    colors[repo_number] = "yellow"
                    GPIO.output(GPIO_map2[0], GPIO.LOW)
                    GPIO.output(GPIO_map2[1], GPIO.HIGH)
                    GPIO.output(GPIO_map2[2], GPIO.LOW)
                sleep(1)

main()
