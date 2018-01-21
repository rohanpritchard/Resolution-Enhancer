# Resolution-Enhancer
An ML photo resolution enhancing messenger bot, built with Python.

## Creating an MVP
There's a number of areas of this project that will take some work, in order to keep me on track, I will aim to build a 'Minimum Viable Product', something that does what I've promised but it shouldn't take me too long to get there.

My MVP will take a bicubic interpolation approach. Note that this is not an ML approach, think of this model not as 'hallucinating' the information that is missing (like a succesful ML approach), but instead smoothing the pixels in an intelligent way to try to improve the quality of an image. This will clearly not be as effective as a decent ML approach, however it will go some of the way towards building the infrastructure required to develop a more aadvanced system.

## The ML Approach
The general idea of the ML approach will be to develop a Generative Adversarial Network (GAN). The reason this is required, is because of the effectiveness of a standard loss function (or lack of, anyway).

With a standard neural network approach, in order to impement back propagation when we're training the model, we need a loss function. This loss function compares the real result to the result that the network has created, and tells the model what parts of the network it needs to 'fine tune'. The trouble with most loss functions for picture enhancement (for instance summing the absolute difference between the pixels of the real target image and the generated one), is that the network will try to develop a solution that minimises the error in the most 'general' way. For example if the generated image generates a line that is one row of pixels away from where it should be, instead of learning to shift that line, it will probably just blur the line so that the error is minimised. What we end up with, is yet another blurred image, just like our bicubic interpolation approach. We need a loss function which, instead, is looking for sharp realistic images, not just something that's looking for the smallest error between the real image and the generated one. How about say, another neural network?

This approch is exactly how GANs work. We'll develop a 'generator' model to develop the pictures, and a 'discriminator' model to decide whether that picture looks realistic. So the first model's aim is to develop photos which are so realistic they fool the discriminator, and the second model's aim is to identify which pictures are fake so well, that it will always be able to tell which one is generated. The discriminator well then tell the generator how it knew it to be fake, and this is how the generator will know what to work on.

A nice analogy to this is an art forger, and an art critic. The art forger is always looking to develop a realistic painting, and the critic is always looking to find the fakes. If the critic can tell the forger what it is about his paintings that make them fake, and the forger keeps developing better and better quality fakes that the critic can keep looking at, both people get better and better at their jobs.

Once the generator model is trained, we take it out of the GAN, and use it by itself. Done.
