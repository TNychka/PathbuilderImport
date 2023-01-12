import json
from json import JSONDecodeError

import utils


class Exporter:
    def __init__(self):
        """LOAD CONFIG"""
        print("LOADING CONFIG")
        try:
            with open("./config.json", "r") as config_file:
                self.config = json.loads(config_file.read())
        except IOError as exc:
            print("Failed to find config.json at ./config.json EXCEPTION: '" + str(exc))
            exit()
        except JSONDecodeError as exc:
            print("Failed to parse config.json at ./config.json EXCEPTION: '" + str(exc))
            exit()

        """LOAD PATHBUILDER"""
        print("LOADING PATHBUILDER JSON")
        try:
            pathbuilder_file_path: str = self.config["pathbuilder_config"]["target_json_path"]
            with open(pathbuilder_file_path, "r") as pathbuilder_file:
                self.pathbuilder = json.loads(pathbuilder_file.read())
        except IOError as exc:
            print("Failed to find pathbuilder json at ''" + pathbuilder_file_path + "'' EXCEPTION: '" + str(exc))
            exit()
        except JSONDecodeError as exc:
            print("Failed to parse pathbuilder json at '" + pathbuilder_file_path + "' EXCEPTION: '" + str(exc))
            exit()

        foundry_config: dict = self.config["foundry_config"]
        """LOAD ANCESTRY PACKS"""
        if "ancestry_packs" in foundry_config:
            print("ANCESTRY DICTIONARY FOUND - LOADING ANCESTRY PACKS")
            try:
                ancestry_pack_files: list[str] = foundry_config["ancestry_packs"]
                self.foundry_ancestries = list()
                for ancestry_pack_path in ancestry_pack_files:
                    with open(ancestry_pack_path, "r") as ancestry_pack_file:
                        while True:
                            line = ancestry_pack_file.readline()
                            if not line:
                                break
                            self.foundry_ancestries.append(json.loads(line))
            except IOError as exc:
                print("Failed to find ancestry pack json at '" + ancestry_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
            except JSONDecodeError as exc:
                print("Failed to parse ancestry pack json at '" + ancestry_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
        else:
            print("NO ANCESTRY DICTIONARY FOUND")

        """LOAD HERITAGE PACKS"""
        if "heritage_packs" in foundry_config:
            print("HERITAGE DICTIONARY FOUND - LOADING HERITAGE PACKS")
            try:
                heritage_pack_files: list[str] = foundry_config["heritage_packs"]
                self.foundry_heritages = list()
                for heritage_pack_path in heritage_pack_files:
                    with open(heritage_pack_path, "r") as heritage_pack_file:
                        while True:
                            line = heritage_pack_file.readline()
                            if not line:
                                break
                            self.foundry_heritages.append(json.loads(line))
            except IOError as exc:
                print("Failed to find heritage pack json at '" + heritage_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
            except JSONDecodeError as exc:
                print("Failed to parse heritage pack json at '" + heritage_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
        else:
            print("NO HERITAGE DICTIONARY FOUND")

        """LOAD FEAT PACKS"""
        if "feat_packs" in foundry_config:
            print("FEAT DICTIONARY FOUND - LOADING FEAT PACKS")
            try:
                feat_pack_files: list[str] = foundry_config["feat_packs"]
                self.foundry_feats = list()
                for feat_pack_path in feat_pack_files:
                    with open(feat_pack_path, "r") as feat_pack_file:
                        while True:
                            line = feat_pack_file.readline()
                            if not line:
                                break
                            self.foundry_feats.append(json.loads(line))
            except IOError as exc:
                print("Failed to find feat pack json at '" + feat_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
            except JSONDecodeError as exc:
                print("Failed to parse feat pack json at '" + feat_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
        else:
            print("NO FEAT DICTIONARY FOUND")

        """LOAD ITEM PACKS"""
        if "item_packs" in foundry_config:
            print("ITEM DICTIONARY FOUND - LOADING ITEM PACKS")
            try:
                item_pack_path: list[str] = foundry_config["item_packs"]
                self.foundry_items = list()
                for item_pack_path in item_pack_path:
                    with open(item_pack_path, "r") as item_pack_file:
                        while True:
                            line = item_pack_file.readline()
                            if not line:
                                break
                            self.foundry_backgrounds.append(json.loads(line))
            except IOError as exc:
                print("Failed to find item pack json at '" + item_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
            except JSONDecodeError as exc:
                print("Failed to parse item pack json at '" + item_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
        else:
            print("NO ITEM DICTIONARY FOUND")

        """LOAD BACKGROUND PACKS"""
        if "background_packs" in foundry_config:
            print("BACKGROUND DICTIONARY FOUND - LOADING BACKGROUND PACKS")
            try:
                background_pack_paths: list[str] = foundry_config["background_packs"]
                self.foundry_backgrounds = list()
                for background_pack_path in background_pack_paths:
                    with open(background_pack_path, "r") as item_pack_file:
                        while True:
                            line = item_pack_file.readline()
                            if not line:
                                break
                            self.foundry_backgrounds.append(json.loads(line))
            except IOError as exc:
                print("Failed to find item pack json at '" + background_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
            except JSONDecodeError as exc:
                print("Failed to parse item pack json at '" + background_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
        else:
            print("NO ITEM DICTIONARY FOUND")

        print("LOADING SUCCESSFUL.")

    def convert_ancestries(self, wipe_current: bool):
        new_pathbuilder_ancestries = []
        for foundry_ancestry in self.foundry_ancestries:
            pathbuilder_ancestry = dict()
            pathbuilder_ancestry["name"] = foundry_ancestry["name"]
            pathbuilder_ancestry["id"] = foundry_ancestry["_id"]  # id doesn't actually appear to matte

            traits_list = ["3rd Party"]
            for trait in foundry_ancestry["system"]["traits"]["value"]:
                if trait[:3] == "hb_":
                    trait = trait[3:]
                traits_list.append(trait)
            if foundry_ancestry["system"]["traits"]["rarity"] != "common":
                traits_list.append(foundry_ancestry["system"]["traits"]["rarity"])
            pathbuilder_ancestry["traits"] = ", ".join(traits_list)

            pathbuilder_ancestry["hp"] = foundry_ancestry["system"]["hp"]
            pathbuilder_ancestry["size"] = utils.size_mapping(foundry_ancestry["system"]["size"])
            pathbuilder_ancestry["speed"] = foundry_ancestry["system"]["speed"]

            pathbuilder_stat_list = []
            pathbuilder_free_boosts = 0
            for key in foundry_ancestry["system"]["boosts"]:
                foundry_stat_list = foundry_ancestry["system"]["boosts"][key]["value"]
                # Is this correct? Probably not. Close enough.
                if not foundry_stat_list:
                    continue
                elif len(foundry_stat_list) == 1:
                    pathbuilder_stat_list.append(utils.stat_mapping(foundry_stat_list[0]))
                else:
                    pathbuilder_free_boosts += 1
            pathbuilder_ancestry["freeBoosts"] = pathbuilder_free_boosts
            pathbuilder_ancestry["abilityBoosts"] = pathbuilder_stat_list

            pathbuilder_stat_list = []
            for key in foundry_ancestry["system"]["flaws"]:
                foundry_stat_list = foundry_ancestry["system"]["flaws"][key]["value"]
                # Is this correct? Probably not. Close enough.
                if not foundry_stat_list:
                    continue
                elif len(foundry_stat_list) == 1:
                    pathbuilder_stat_list.append(utils.stat_mapping(foundry_stat_list[0]))
            pathbuilder_ancestry["abilityFlaws"] = pathbuilder_stat_list

            pathbuilder_ancestry["description"] = foundry_ancestry["system"]["description"]["value"]
            pathbuilder_ancestry["languages"] = ", ".join(foundry_ancestry["system"]["languages"]["value"])
            pathbuilder_ancestry["src"] = foundry_ancestry["system"]["source"]["value"]
            pathbuilder_ancestry["databaseID"] = 1
            new_pathbuilder_ancestries.append(pathbuilder_ancestry)
        if wipe_current:
            self.pathbuilder["listCustomAncestries"] = new_pathbuilder_ancestries
        else:
            self.pathbuilder["listCustomAncestries"].append(new_pathbuilder_ancestries)

    def write_new_pathbuilder_json(self):
        pathbuilder_file_path: str = self.config["pathbuilder_config"]["target_json_path"]
        with open(pathbuilder_file_path, "w") as pathbuilder_file:
            json.dump(self.pathbuilder, pathbuilder_file, indent=4)


def main():
    exporter = Exporter()
    exporter.convert_ancestries(True)
    exporter.write_new_pathbuilder_json()


if __name__ == "__main__":
    main()
