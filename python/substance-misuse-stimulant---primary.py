# Kathryn M Abel, Holly Hope, Eleanor Swift, Rosa Parisi, Darren M Ashcroft, Kyriaki Kosidov, Semre Su Osam, Christian Dolman, Mathias Pierce, 2024.

import sys, csv, re

codes = [{"code":"E257.11","system":"readv2"},{"code":"E257z00","system":"readv2"},{"code":"E244300","system":"readv2"},{"code":"E257100","system":"readv2"},{"code":"E244z00","system":"readv2"},{"code":"E257300","system":"readv2"},{"code":"E244100","system":"readv2"},{"code":"E257.12","system":"readv2"},{"code":"E244200","system":"readv2"},{"code":"E244011","system":"readv2"},{"code":"E257.00","system":"readv2"},{"code":"E257000","system":"readv2"},{"code":"E244z11","system":"readv2"},{"code":"Eu15211","system":"readv2"},{"code":"E257200","system":"readv2"},{"code":"E244.12","system":"readv2"},{"code":"E244.00","system":"readv2"},{"code":"E244000","system":"readv2"},{"code":"E244.11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('substance-misuse-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["substance-misuse-stimulant---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["substance-misuse-stimulant---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["substance-misuse-stimulant---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
