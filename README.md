```
{
    "pathbuilder_config" : {
        "target_json_path" : ""
    },
    "foundry_config" : {
        "ancestry_packs" : [],
        "heritage_packs" : [],
        "items_packs" : [],
        "feat_packs" : []
    }
}
```

target_json_path: str. Absolute path of the pathbuilder_config json.
example: "/home/user/documents/pathbuilder_pack.json"

ancestry_packs: list[str]. List of absolute paths of foundry compendiums to export as ancestries. Foundry compendium must only contain ancestries.
example: ["/home/user/documents/ancestries_one.json", "/home/user/documents/ancestries_two.json"]

heritage_packs: list[str]. List of absolute paths of foundry compendiums to export as heritages. Foundry compendium must only contain heritages.
example: ["/home/user/documents/heritages_one.json", "/home/user/documents/heritages_two.json"]

feat_packs: list[str]. List of absolute paths of foundry compendiums to export as feats. Foundry compendium must only contain feats.
example: ["/home/user/documents/feats_one.json", "/home/user/documents/feats_two.json"]

item_packs: list[str]. List of absolute paths of foundry compendiums to export as items. Foundry compendium must only contain items.
example: ["/home/user/documents/items_one.json", "/home/user/documents/items_two.json"]