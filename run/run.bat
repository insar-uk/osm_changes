cd C:\Users\user\Documents\osm_changes

set "layer1 = "201610" "201704" "
set "layer2 = "201704" "201710" "
set "output_path = "output1" "output2" "


for %%a %%b %%c in (%layer1%) (%layer2%) (%output_path%)

    python -m iterate %%a %%b %%c 

    python -m osm_changes