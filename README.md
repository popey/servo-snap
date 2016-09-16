**Mozilla Servo Snap**

*Notes*

 * Servo is a new browser engine from Mozilla in early development
 * I had to make a plugin to build Servo using Rust build tools
 * It takes a long time to build
 * The codegen-units setting in x-servo.py plugin can be used to limit how many build processes you run (like make -j4)

*Building*

On an up-to-date 16.04 system, install snapcraft and run snapcraft in the same directory as this README

*Things which work*

* Servo builds (sometimes) - typically tip of git breaks now and then, the homu-tmp branch usually builds though

*Things which don't work*

 * Launching Servo (with the `runservo` command) once built and installed doesn't work, but fails with `"XOpenIM Failed"`
 * Currently (2016-09-16) Servo fails to build. Something changed, perhaps missing dependency. Here's the [build log](http://paste.ubuntu.com/23185989/)  line 2808 onwards is the interesting bit.
