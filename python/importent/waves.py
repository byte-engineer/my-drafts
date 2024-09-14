# importent\waves.py

import math
import librosa as rs
import soundfile
import  numpy as np
import matplotlib.pyplot as plt
from os import system
import os
from time import time as tm
system("cls")
print("Importing Finished")




class helpers:


    def __init__(self, samplearte):
        self.samplerate = samplearte
        print(f"object created: helpers")


    def sample_to_time(self, samples :int) -> float:
         return float(samples / self.samplerate)
    

    def time_to_samples(self, time :float) -> int:
        return int(time * self.samplerate)
    

    def info(data, show= True):
        try:
            type = type(data)
        except:
            print("Data failed.")
            type = None
        try:
            leng = len(data)
        except:
            print("length failed")
            leng = None
            
        if show == True:
            print(data)
        print("-"*10)
        print(f"Type: {type}\nlength: {leng}")
    def timeit(*func):
        def edited(*args):
            tm1= tm()
            func(*args)
            print("-"*10, f"\n{tm()-tm1}")
        return edited
    
    def save(self, path, wave: np.ndarray):
        soundfile.write(path, wave, self.samplerate)



class func:


    def __init__(self) -> None:
        print(f"object created: func")


    def sin(X: float, frequency: float= 1) -> complex:
        return complex(math.e**(frequency * 1J * X )).imag
    

    def softmax(z:list):
        return  (np.e**np.array(z)/sum(np.e**np.array(z)))
    

    def sigmoid(self, X, hscaling= 0.1) -> float:
        X *= hscaling
        return 1 / (1 + ((math.e)**-X))
    

    def square(self, X:float, hscaling= 0.1) -> int:
        X *= hscaling
        if X > 0:
            return float(-1)
        return float(1)
    

    def hyperbolic_tan(self, X:float, hscaling= 0.1) -> float:
        X *= hscaling
        return (((math.e**X) - (math.e**-X))) / (((math.e**X) + (math.e**-X))) 


    def invert(self, X, hscaling= 0.1):
        X *= hscaling
        return X


    def non(self, X, hscaling= 0.1):
        X *= hscaling
        return X


class generate():
    def __init__(self, samplerate) -> None:
        self.func = func()
        self.hlps = helpers(samplerate)
        self.samplerate = samplerate
        print(f"object created: generate")


    def square(self, time, frequency,top= 1, bottom= -1, scale= 1, invert= False):
        length = self.hlps.time_to_samples(time)
        factor = frequency*(2*math.pi/self.samplerate)
        inversion = -1 if invert else 1
        return np.array([float(top if math.sin(i * factor)>=0 else bottom) for i in range(length)])*scale*inversion
    

    def sin(self, time, frequency, scale= 1, invert= False):
        length = self.hlps.time_to_samples(time)
        factor = frequency*(2*math.pi/self.samplerate)
        inversion = -1 if invert else 1
        return np.array([(math.sin(i * factor)) for i in range(length)])*scale*inversion
    

    def cos(self, time, frequency, scale= 1, invert= False):
        length = self.hlps.time_to_samples(time)
        factor = frequency*(2*math.pi/self.samplerate)
        inversion = -1 if invert else 1
        return np.array([(math.cos(i * factor)) for i in range(length)])*scale*inversion


    def triangle(self, time, frequency, scale=1, invert= False):
        length = time * self.samplerate
        top = (self.samplerate / 4) / frequency
        inversion = 1 if invert else -1
        up = np.linspace(0, 1, int(top), endpoint=False)
        down = np.linspace(1, -1, int(top*2), endpoint=False)
        final_up = np.linspace(-1, 0, int(top), endpoint=False)
        period = np.concatenate((up, down, final_up))
        num_periods = int(np.ceil(length / period.size))
        triangle_wave = np.tile(period, num_periods)
        return triangle_wave[:int(length)] * -inversion * scale


    def AM(self, massage, carrier_fre: int, scale: float= 1, invert= False):
        inversion = 1 if invert else -1
        massage = np.array(massage, dtype= "float32")
        sine = self.sin(self.hlps.sample_to_time(len(massage)), carrier_fre)
        return sine * massage * scale * inversion
    

    def sin_AM(self,time: float, massage: float, carrier: float, scale: float= 1):
        return self.sin(time, massage, scale= scale) * self.sin(time, carrier, scale= scale)


    def sin_FM(self, time:float, massage_freq: float, carrier_fre: float, mod_per:float, scale: float= 1):
        mod = carrier_fre*mod_per
        const = (2*math.pi/self.samplerate)
        return np.array([scale*math.cos((const*carrier_fre * t) + mod * math.sin(const*massage_freq*t)) for t in range(time*self.samplerate)])


    def FM(self, massage, carrier_fre: float, mod:float, scale: float= 1):
        const = (2*math.pi/self.samplerate)
        return np.array([scale*math.cos((const*carrier_fre*t) + mod * massage[t] ) for t in range(massage.shape[0])])
    
class Noise:


    def __init__(self, samplerate) -> None:
        self.samplerate = samplerate
        print("object created: Noise")


    def noise_deform(self, time, main_freq, num_frequencies = 50, amplitude = 1, factor= 1):
        size = self.samplerate * time
        x = np.linspace(0, main_freq * np.pi, size)
        noise_wave = np.zeros(size)
    # Generate the wave
        for i in range(0, num_frequencies):
            frequency = np.random.uniform(0, 1)
            phase = np.random.uniform(0, 2 * np.pi)
            noise_wave += amplitude * np.sin(frequency * x + phase) # main part
    # Normalize
        noise_wave /= num_frequencies
        return noise_wave * factor
    

    def normal(self, time, window_size=10, smooth=3, offset= 0, width= 1):

        size = time*self.samplerate
        noise_wave = np.random.normal(offset, width, size +(smooth*(window_size-1))+1)

        if smooth:
            smoothed_wave = np.convolve(noise_wave, np.ones(window_size)/window_size, mode='valid')
            
            for i in range(smooth-1):
                smoothed_wave = np.convolve(smoothed_wave, np.ones(window_size)/window_size, mode='valid')
        return smoothed_wave


class stringEncoder:

    def __init__(self):
        print("object created: stringEncoder")


    def toInts(self, text: str) -> list[int]:
        container = []
        for letter in text:
            container.append(ord(letter))
        return container

    def toBins(self, text) -> list[str]:
        ints = self.toInts(text)  # Assuming toInts is a method that converts text to integers
        bins = []

        for item in ints:
            ZO = bin(item)[2:]  # Convert integer to binary string, strip '0b'

            # Pad with leading zeros to make each binary string length a multiple of 8
            while len(ZO) % 8 != 0:
                ZO = '0' + ZO
            bins.append(ZO)
        return bins

    def toBin(self, text: str, sep= ' '):
        bins = self.toBins(text)
        OZ = []

        # Process each binary element in chunks of 8 bits
        for element in bins:
            for i in range(0, len(element), 8):  # Increment by 8 to get 8-bit chunks
                OZ.append(element[i:i+8])

        return sep.join(OZ)


class binWaveDecode(stringEncoder):
    def __init__(self, samplerate, freq):
        print("object created: binWaveDecode")
        self.freq = freq
        self.samplerate = samplerate


    def binSin(self, text):
        Bin = self.toBin(text, sep= '')

        gen = generate(self.samplerate)
        wav = gen.sin(1/self.freq, self.freq)  # Generates a sine wave of duration 1/frequency

        array = np.array([])

        for B in Bin:
            if B == '1':
                array = np.concatenate([array, wav])
            else:
                array = np.concatenate([array, -wav])

        return array



class analysis:

    def __init__(self, samplerate) -> None:
        self.samplerate = samplerate
        print("object created: Noise")


    def show_fft(self, data: np.ndarray):

        fft = np.fft.fft(data)
        leng = len(data)
        fft = fft[:leng//2]

        T = 1/self.samplerate  # Sampling interval
        frequencies = np.fft.fftfreq(leng, T)[:leng//2]
        
        plt.stem(frequencies, np.abs(fft), 'r', markerfmt=" ", basefmt="-b")
        plt.title('FFT of the Signal')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Magnitude')
        plt.show()




def Addition(func):
    def edited(*arg, **kwarg):
        start = tm()
        func(*arg, **kwarg)
        end   = tm()
        print(f"------------------------\ntime: {(end-start).__round__(2)} Second")
    return edited

@Addition
def main():
    sample_rate   = 44100

    path0 = r"C:\Users\Hp\Desktop\bilal\files\Codes\Python\Results\Audio\test0.wav"
    path1 = r"C:\Users\Hp\Desktop\bilal\files\Codes\Python\Results\Audio\test1.wav"
    path2 = r"C:\Users\Hp\Desktop\bilal\files\Codes\Python\Results\Audio\test2.wav"
    os.chdir("..")
    print("path:", __file__)

    # gen = generate(sample_rate)
    # nis = Noise(sample_rate)
    anls = analysis(sample_rate)
    # enco = stringEncoder()
    waver = binWaveDecode(sample_rate, 500)

    wave0 = waver.binSin(input('>> '))
    # Examples
    # wave0 = gen.sin(5, 1000)
    # wave1 = nis.noise_deform(3, 16000)
    # wave2 = nis.normal(3, smooth= 10)

    anls.show_fft(wave0)

    # Store in 
    soundfile.write(path0, wave0, sample_rate)
    # soundfile.write(path1, wave1, sample_rate)
    # soundfile.write(path2, wave2, sample_rate)

if __name__ == "__main__":
    main()
