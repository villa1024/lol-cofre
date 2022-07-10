array_cofres = ["zed", "xayah", "vayne", "varus", "tristana", "senna", "quinn", "miss fortune", "lux", "lucian", "kalista", "kaisa", "jinx", "jhin", "gnar", "ezreal", "caitlyn", "bardo", "ashe", "aphelios", "akshan"]
array_campeones = ["zyra", "zeri", "zed", "yuumi", "xerath", "warwick", "vi", "velkoz", "veigar", "twitch", "thresh", "teemo", "taric", "sylas", "swain", "soraka", "sona", "sona", "sivir", "shen", "samira", "ryze", "riven", "renekton", "renata", "rell", "reksai", "rakan", "pyke", "pantheon", "oriana", "olaf", "nunu", "nocturne", "nautilus", "nasus", "nami", "morgana", "mordekaiser", "malphite", "maestro yi", "leona", "leblanc", "kogmaw", "khazix", "kayn", "karma", "jayce", "jax", "janna", "gwen", "graves", "garen", "gangplank", "fizz", "evelynn", "ekko", "dr mundo", "draven", "darius", "camille", "braum", "brand", "blitzcrank", "annie", "amumu", "alistar", "akali", "ahri", "atrox", "xayah", "vayne", "varus", "tristana", "senna", "quinn", "miss fortune", "lux", "lucian", "kalista", "kaisa", "jinx", "jhin", "gnar", "ezreal", "caitlyn", "bardo", "ashe", "aphelios", "akshan"]
campeon = input()
if campeon in array_campeones:
    if campeon in array_cofres:
        print("Ya tienes cofre")
    else:
        print("No tienes cofre")
else:
    print("no tienes al campeon")