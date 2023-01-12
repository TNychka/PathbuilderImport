import json
from json import JSONDecodeError

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
                self.ancestry_packs = list()
                for ancestry_pack_path in ancestry_pack_files:
                    with open(ancestry_pack_file, "r") as ancestry_pack_file:
                        self.ancestry_packs.append(json.loads(pathbuilder_file.read()))
            except IOError as exc:
                print("Failed to find ancestry pack json at '" + ancestry_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
            except JSONDecodeError as exc:
                print("Failed to parse pathbuilder json at '" + ancestry_pack_path + "' EXCEPTION: '" + str(exc))
                exit()

        """LOAD HERITAGE PACKS"""
        if "heritage_packs" in foundry_config:
            print("HERITAGE DICTIONARY FOUND - LOADING HERITAGE PACKS")
            try:
                heritage_pack_files: list[str] = foundry_config["heritage_packs"]
                self.heritage_packs = list()
                for heritage_pack_path in heritage_pack_files:
                    with open(heritage_pack_file, "r") as heritage_pack_file:
                        self.heritage_packs.append(json.loads(pathbuilder_file.read()))
            except IOError as exc:
                print("Failed to find heritage pack json at '" + heritage_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
            except JSONDecodeError as exc:
                print("Failed to parse pathbuilder json at '" + heritage_pack_path + "' EXCEPTION: '" + str(exc))
                exit()

        """LOAD FEAT PACKS"""
        if "feat_packs" in foundry_config:
            print("FEAT DICTIONARY FOUND - LOADING FEAT PACKS")
            try:
                feat_pack_files: list[str] = foundry_config["feat_packs"]
                self.feat_packs = list()
                for feat_pack_path in feat_pack_files:
                    with open(feat_pack_file, "r") as feat_pack_file:
                        self.feat_packs.append(json.loads(pathbuilder_file.read()))
            except IOError as exc:
                print("Failed to find feat pack json at '" + feat_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
            except JSONDecodeError as exc:
                print("Failed to parse pathbuilder json at '" + feat_pack_path + "' EXCEPTION: '" + str(exc))
                exit()

        """LOAD ITEM PACKS"""
        if "item_packs" in foundry_config:
            print("ITEM DICTIONARY FOUND - LOADING ITEM PACKS")
            try:
                item_pack_files: list[str] = foundry_config["item_packs"]
                self.item_packs = list()
                for item_pack_path in item_pack_files:
                    with open(item_pack_file, "r") as item_pack_file:
                        self.item_packs.append(json.loads(pathbuilder_file.read()))
            except IOError as exc:
                print("Failed to find item pack json at '" + item_pack_path + "' EXCEPTION: '" + str(exc))
                exit()
            except JSONDecodeError as exc:
                print("Failed to parse pathbuilder json at '" + item_pack_path + "' EXCEPTION: '" + str(exc))
                exit()

        print("LOADING SUCCESSFUL.")
        

def main():
    exporter = Exporter()
    print("bleh")
        
if __name__ == "__main__":
    main()
