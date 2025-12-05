# cartify

cartify is a work-in-progress tool to automate the setup of custom icons for the Nintendo switch [cartify-theme](https://github.com/StankWizardLizard/cartify-theme)

## Getting Started

Before we can get started with using this tool you need to make sure you have dumped your titles from your swith into a titles.csv file, this program supports an extra feature where it will paste the cartridge code of the game if the entry is present in the titles.csv file, see example:

```
Title Code|Title ID|Title Name
LA-H-AW7KA-EUR|01001F5010DFA000|Pokémon Legends: Arceus
LA-H-ALZXA-EUR|0100A3D008C5C000|Pokémon Scarlet
LA-H-AAAAA-EUR|01007EF00011E000|The Legend of Zelda: Breath of the Wild
LA-H-AAAAB-EUR|0100F2C0115B6000|The Legend of Zelda: Tears of the Kingdom
|0100C9A00ECE6000|Nintendo 64 - Nintendo Switch Online
|010012F017576000|Game Boy Advance – Nintendo Switch Online
```

If the Title Code entry is blank the program will simply just ignore it, feel free to put whatever cartridge code youd like.

### Prerequisites

This tool is reliant on two other tools [sys-tweak](https://sodasoba1.github.io/sys-tweak/) and [nx-titles-list-dumper](https://github.com/HamletDuFromage/nx-titles-list-dumper), make sure you are well informed on these other tools before continuing.

### Installing

```
# clone repo
git clone https://github.com/Stank-Wizard/cartify.git

# enter directory
cd cartify

# copy needed files
cp [path-to-your-titles.csv-file] assets/

# finally running the program
make
```

## License

This software is licensed under the terms of the GPLv3, with exemptions for specific projects noted below.

You can find a copy of the license in the [LICENSE file](LICENSE).

## Credits

cartify is currently being developed and maintained by me but i'd like to give credit where credit is due as this couldn't be possible without the following projects:

* __sodasoba1__ for the [sys-tweak](https://sodasoba1.github.io/sys-tweak/) project
* __HamletDuFromage__ for the [nx-titles-list-dumper](https://github.com/HamletDuFromage/nx-titles-list-dumper) project
