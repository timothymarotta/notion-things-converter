from ThingsHelper import ThingsModel

def main():
    print(type(ThingsModel().get_action('paragraph')))

if __name__ == "__main__":
    main()



# Converter needs to parse Notion cURL and return a dictionary {type, children, text}
# TODO need to check child blocks if value == .header or .item or .children (either convert to lists or just throw a single check or check every time)