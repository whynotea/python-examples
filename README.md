# python-examples
A collection of Python coding examples

## kvcalc
A basic calculator application using Kivy and built for Android using buildozer

### Build
`make build`

This builds a local Podman image with the necessary buildozer setup.

It then runs a container using the buildozer image to compile a .apk file in the bin directory. 

### Run
#### Android
Copy the .apk produced in the build stage to your Android phone to install and run the calculator there.

#### Linux
Create a conda environment:

`make conda-create`

Then run locally in the newly created environment:

`make conda-run`
