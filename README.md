# Pokémon Conquest Calculators

This program was created as an unofficial helping tool for the "Pokémon Conquest" video game, and provides a Graphical User Interface designed with two calculators:

* An IV Calculator,
* A Stats Calculator.

There are two files included in this archive:

* ConquestCalculators.py, a Python script containing the algorithm needed to run the interface.
* PokemonData.xml, an XML file containing the **list of every Pokémon species** in the game with their corresponding **Base Stats**.

# Requirements

This program requires to have **Python 3** installed on the computer, as well as the "tkinter" and "math" libraries (those are already included by default with every standard Python installation).

Download Python here: https://www.python.org/downloads/

# Usage

After downloading and installing Python 3, you simply have to download the files and move them wherever you want. Just make sure both files remain together in the **same directory**.

## IV Calculator

The **IV Calculator** allows the user to find out a Pokémon's **IVs**, provided the user knows its **Species**, **Stats**, **Link,** and **Energy**.

First, fill out the fields in the "Stats" and "Energy" frames with the corresponding values.

Since Link acts as a level system in the game, and stats update only when the integer part increases, only the integer part needs to be specified in the "Link" field.

For example, if the Pokémon's Link is **15.43%**, just put **15** instead of **15.43**. The algorithm will however still work **regardless** if you put the exact Link value or not.

Then, select the **Pokémon species** in the corresponding dropdown menu. 
The Pokémon are ordered in the same order as the "Collection" section of the game (From "Eevee" to "Rayquaza"). You can also type the first letters of the Pokémon's species to narrow the selection down.

For example, if you type "E", the menu will now only display the Pokémon whose names start with the letter "E", aka:

* Eevee
* Espeon
* Ekans
* Emboar
* Empoleon
* Excadrill
* Emolga

Once everything is set, click on the "Calculate IVs" button. The possible IVs for each stat will then be displayed in the "Pokémon IVs" frame.

If there are no possible IVs found for one stat, the program will display an error. In that case, make sure that all input values have been set correctly.

If several calculations need to be done with varying parameters, edit the values accordingly and click on the button for every additional instance to display the updated results.

### Example

We want to know the IVs of an **Igglybuff**, with a Link value of **15.42%**, a **Very High** Energy, and the following stats:

* HP: 50
* Atk: 12
* Def: 11
* Spe: 4

The calculator returns the following results:

* HP: 17-23
* Atk: 9-14
* Def: 28-31
* Spe: Err

After checking once again, it turns out the Speed stat was **5** instead of 4. Correcting the entries then returns the following results:


* HP: 17-23
* Atk: 9-14
* Def: 28-31
* Spe: 0-4

## Stats Calculator

The **Stats Calculator** allows the user to find out a Pokémon's **Stats**, provided the user knows the **Species**, **IVs**, **Link**, and **Energy**.

First, fill out the fields in the "IVs" and "Energy" frames with the corresponding values. Make sure that the IV values are between **0** and **31**.

The "Link" and "Pokémon" fields work the same as for the IV Calculator.

Once everything is set, click on the "Calculate Stats" button. The resulting values for each stat will then be displayed in the "Pokémon Stats" frame.
If more calculations need to be done with other parameters, edit the values accordingly and click on the button for every additional instance to display the results.

### Example

We want to know the stats of a **Jolteon** with **perfect IVs** (31 in every stat), a Link Value of **70%** and **Medium** Energy. The calculator returns the Following results:

* HP: 189
* Atk: 179
* Def: 133
* Spe: 207

