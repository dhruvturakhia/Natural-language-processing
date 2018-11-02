from chemdataextractor import Document
import time



def extract_all_chem_names(read_path = "", write_in_file = False):
    start_time = time.time()
    doc = None

    #Always open files as binary
    print(f"\nLoading the information from: {read_path}.....")
    with open(read_path, "rb") as f:
        doc = Document.from_file(f)
        f.close()
    print("Document is created")


    print("\nExtracting all chemical names in the document.....")
    #records ==> records of all mentions and abbreviations, properties and spectra
    #Concatenate all the chemical names in the list
    all_chemicals = []
    for compound in doc.records:
        comp = compound.serialize()
        if "names" in comp:
            all_chemicals += comp["names"]

    all_chemicals.sort()
    total_chems = len(all_chemicals)
    print(f"The total number of chemical names extracted are {total_chems}")

    if (write_in_file):
        write_path = read_path.split(".")[0] + "_chem_list.txt"
        print(f"\nWriting the information to file {write_path}")
        with open(write_path, "w+") as f:
            for chemical in all_chemicals:
                f.write(chemical + "\n")
            f.close()

    tot_time = round(time.time() - start_time, 3)
    print(f"\nTime taken to extract all the chemical name from the doc is {tot_time} seconds")

    return all_chemicals;


read_path = "test.txt"
extract_all_chem_names(read_path, write_in_file = True)
