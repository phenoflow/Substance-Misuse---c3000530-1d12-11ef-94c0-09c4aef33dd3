# Kathryn M Abel, Holly Hope, Eleanor Swift, Rosa Parisi, Darren M Ashcroft, Kyriaki Kosidov, Semre Su Osam, Christian Dolman, Mathias Pierce, 2024.

import sys, csv, re

codes = [{"code":"1V0C.00","system":"readv2"},{"code":"1V07.00","system":"readv2"},{"code":"9G23.00","system":"readv2"},{"code":"Eu11212","system":"readv2"},{"code":"Eu18211","system":"readv2"},{"code":"8B23.00","system":"readv2"},{"code":"Eu14211","system":"readv2"},{"code":"Eu12211","system":"readv2"},{"code":"E24..11","system":"readv2"},{"code":"Eu11211","system":"readv2"},{"code":"9G24.00","system":"readv2"},{"code":"Eu19211","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('substance-misuse-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["substance-misuse-addict---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["substance-misuse-addict---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["substance-misuse-addict---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
