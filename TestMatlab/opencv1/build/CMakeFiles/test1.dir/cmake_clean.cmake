file(REMOVE_RECURSE
  "test1.pdb"
  "test1"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/test1.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
