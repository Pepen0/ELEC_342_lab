# Lab 1: 

# Lab 2: 

# Lab 3: Introduction to Programming



# Lab 4: Simulink and Filter Design using MATLAB

## Key concepts:

### sound function:
- The sound function plays audio signals that have values normalized within the range [-1, 1]. If a signal exceeds this range, it will be clipped.
- `sound(y, Fs)`

#### Amplitude Scaling with the sound function
- Amplitude scaling is a technique used to adjust the amplitude/volume of a signal to a desired value.
- `sound(amplitude * y, Fs)` where `amplitude` is a scalar value.


#### Frequency sampling with the sound function
- The frequency sampling technique is a technique used to create a signal with a specific frequency.
- `sound(y, Fs * speed_factor)` where `speed_factor` is a scalar value.

#### Clipping Behavior:
- The clipping behavior of the sound function is that if the signal exceeds the range [-1, 1], it will be clipped to [-1, 1].

#### Sampling rate perception:
- Manipulation of the sampling rate can affect the perception of speend and pitch.

### Digital Filter Design:
- A digital filter is a mathematical model that processes digital signals.
- #### Butterworth Filter:
    - flat passband with no ripple
- #### Chebyshev Filter Type 1
    - flat passband with equal ripple
- #### FIR Filter (using Blackman window)
    - stable and habe linear phase response

### Filter specifications:
```
- Passband Frequency: 1000 Hz
- Stopband Frequency: 1400 Hz
- Sampling Rate: 8000 Hz
- passband ripple: 1 dB
- stopband attenuation: 80 dB
```

### Matlab FDATOOL
- Step 1: Specify filter type and parameters
- Step 2: Analyze filter Response
- Step 3: Export filter coefficients

### Analysis Metrics:
#### Filter Order:
- IIR(Butterworth/Chebyshev) have lower order than FIR for the same specifications.

#### Memory annd Computational costs:
- IIR(Butterworth/Chebyshev) are more efficient in memory and computational costs than FIR since they have lower order.
- FIR provide a more stable and predictable phase response.

### Rounding coeffiicents and pole zero plots:

#### Effect of rounding:
- introduction of quantization error
may shift slightly the original indicating changes in stability or frequency response.

#### Pole-zero plots in mathlab:
- `zplane(b, a)` to visualise poles and zeros of the transfer function `H(z) = b(z)/a(z)`

#### Floating point representation:
- IEEE 754 representation of real numbers can cause rounding errors due to the limited precision of the floating point representation.
- `0.1 + 0.1 + 0.1 = 0.30000000000000004` in binary representation.