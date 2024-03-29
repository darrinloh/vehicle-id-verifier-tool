# Vehicle ID verifier tool

Simple script to find out the possible combinations of a Singapore vehicle ID,
given missing digits and letters.

For example:
SND1838G
Assuming we don't know the substring D1 (SN**838G).

The script will return all possible valid combinations that matches with the provided partial vehicle.

## How to use

1. Run `python main.py`
2. Script will prompt user to input vehicle ID
   1. User has to replace the missing letter with * and missing digit with _
   2. Example: SN*_838G
3. Script will print out the possible combinations for you.

## Caveat
1. Currently only work for cars, starting with prefix S.

## Feature improvements
1. Support prefix E for car type
2. Support motorbike and large vehicle types

## Contribution
Do feel free to create merge requests to fix bugs, or add new features
