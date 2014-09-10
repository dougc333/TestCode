pom.xml supports both java and scala producer/consumer examples

run unit tests by default, integration tests separated from unit tests by directory 

2 profiles, 
1) dev profile for unit tests
2) integration test profile for integration tests

2 goals
1) disable integration tests in development profile
2) disable unit tests in integration test profile

3 properties
skip.unit.tests
skip.integration.tests
build.profile.id

configuration of the build profiles
add default values of properties to POM
create new profiles and extend default property values in integration test profile



Step 2: add gradle


