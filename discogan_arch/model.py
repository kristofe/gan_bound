import torch
import torch.nn as nn

kernel_sizes = [4,3,3]
strides = [2,2,1]
paddings=[0,0,1]

latent_dim = 300

class Discriminator(nn.Module):
    def __init__(
            self,
            ):

        super(Discriminator, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, 4, 2, 1, bias=False)
        self.relu1 = nn.LeakyReLU(0.2, inplace=True)

        self.conv2 = nn.Conv2d(64, 64 * 2, 4, 2, 1, bias=False)
        self.bn2 = nn.BatchNorm2d(64 * 2)
        self.relu2 = nn.LeakyReLU(0.2, inplace=True)

        self.conv3 = nn.Conv2d(64 * 2, 64 * 4, 4, 2, 1, bias=False)
        self.bn3 = nn.BatchNorm2d(64 * 4)
        self.relu3 = nn.LeakyReLU(0.2, inplace=True)

        self.conv4 = nn.Conv2d(64 * 4, 64 * 8, 4, 2, 1, bias=False)
        self.bn4 = nn.BatchNorm2d(64 * 8)
        self.relu4 = nn.LeakyReLU(0.2, inplace=True)

        self.conv5 = nn.Conv2d(64 * 8, 1, 4, 1, 0, bias=False)

    def forward(self, input):
        conv1 = self.conv1( input )
        relu1 = self.relu1( conv1 )

        conv2 = self.conv2( relu1 )
        bn2 = self.bn2( conv2 )
        relu2 = self.relu2( bn2 )

        conv3 = self.conv3( relu2 )
        bn3 = self.bn3( conv3 )
        relu3 = self.relu3( bn3 )

        conv4 = self.conv4( relu3 )
        bn4 = self.bn4( conv4 )
        relu4 = self.relu4( bn4 )

        conv5 = self.conv5( relu4 )

        return torch.sigmoid( conv5 ), [relu2, relu3, relu4]


class Generator(nn.Module):
    def __init__(
            self,
            num_layers=4,
            ):

        super(Generator, self).__init__()

        if num_layers == 8:
            self.main = nn.Sequential(
                nn.Conv2d(3, 64, 4, 2, 1, bias=False),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 2, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 4, 64 * 8, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 8),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 8, 64*16, 4, 1, 0, bias=False),
                nn.BatchNorm2d(64*16),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64*16, 64*24, 1, 1, 0, bias=False),
                nn.BatchNorm2d(64*24),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64*24, 64*28, 1, 1, 0, bias=False),
                nn.BatchNorm2d(64*28),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 28, 100, 1, 1, 0, bias=False),
                nn.BatchNorm2d(100),
                nn.LeakyReLU(0.2, inplace=True),

                nn.ConvTranspose2d(100, 64 * 28, 1, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 28),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 28, 64 * 24, 1, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 24),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 24, 64 * 16, 1, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 16),
                nn.ReLU(True),
                nn.ConvTranspose2d(64*16, 64 * 8, 4, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 8),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 8, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 4, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 2,     64, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(True),
                nn.ConvTranspose2d(    64,      3, 4, 2, 1, bias=False),
                nn.Sigmoid()
            )

        if num_layers == 7:
            self.main = nn.Sequential(
                nn.Conv2d(3, 64, 4, 2, 1, bias=False),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 2, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 4, 64 * 8, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 8),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 8, 64*16, 4, 1, 0, bias=False),
                nn.BatchNorm2d(64*16),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64*16, 64*24, 1, 1, 0, bias=False),
                nn.BatchNorm2d(64*24),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64*24, 100, 1, 1, 0, bias=False),
                nn.BatchNorm2d(100),
                nn.LeakyReLU(0.2, inplace=True),

                nn.ConvTranspose2d(100, 64 * 24, 1, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 24),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 24, 64 * 16, 1, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 16),
                nn.ReLU(True),
                nn.ConvTranspose2d(64*16, 64 * 8, 4, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 8),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 8, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 4, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 2,     64, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(True),
                nn.ConvTranspose2d(    64,      3, 4, 2, 1, bias=False),
                nn.Sigmoid()
            )

        if num_layers == 6:
            self.main = nn.Sequential(
                nn.Conv2d(3, 64, 4, 2, 1, bias=False),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 2, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 4, 64 * 8, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 8),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 8, 64*16, 4, 1, 0, bias=False),
                nn.BatchNorm2d(64*16),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64*16, 100, 1, 1, 0, bias=False),
                nn.BatchNorm2d(100),
                nn.LeakyReLU(0.2, inplace=True),

                nn.ConvTranspose2d(100, 64 * 16, 1, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 16),
                nn.ReLU(True),
                nn.ConvTranspose2d(64*16, 64 * 8, 4, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 8),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 8, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 4, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 2,     64, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(True),
                nn.ConvTranspose2d(    64,      3, 4, 2, 1, bias=False),
                nn.Sigmoid()
            )

        if num_layers == 5:
            self.main = nn.Sequential(
                nn.Conv2d(3, 64, 4, 2, 1, bias=False),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 2, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 4, 64 * 8, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 8),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 8, 100, 4, 1, 0, bias=False),
                nn.BatchNorm2d(100),
                nn.LeakyReLU(0.2, inplace=True),

                nn.ConvTranspose2d(100, 64 * 8, 4, 1, 0, bias=False),
                nn.BatchNorm2d(64 * 8),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 8, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 4, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 2, 64, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(True),
                nn.ConvTranspose2d(64, 3, 4, 2, 1, bias=False),
                nn.Sigmoid()
            )

        if num_layers == 4:
            self.main = nn.Sequential(
                nn.Conv2d(3, 64, 4, 2, 1, bias=False),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 2, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 4, 64 * 8, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 8),
                nn.LeakyReLU(0.2, inplace=True),

                nn.ConvTranspose2d(64 * 8, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 4, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 2,     64, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(True),
                nn.ConvTranspose2d(    64,      3, 4, 2, 1, bias=False),
                nn.Sigmoid()
            )

        if num_layers == 3:
            self.main = nn.Sequential(
                nn.Conv2d(3, 64, 4, 2, 1, bias=False),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64 * 2, 64 * 4, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 4),
                nn.LeakyReLU(0.2, inplace=True),

                nn.ConvTranspose2d(64 * 4, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.ReLU(True),
                nn.ConvTranspose2d(64 * 2, 64, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(True),
                nn.ConvTranspose2d(64, 3, 4, 2, 1, bias=False),
                nn.Sigmoid()
            )

        if num_layers == 2:
            self.main = nn.Sequential(
                nn.Conv2d(3, 64, 4, 2, 1, bias=False),
                nn.LeakyReLU(0.2, inplace=True),
                nn.Conv2d(64, 64 * 2, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64 * 2),
                nn.LeakyReLU(0.2, inplace=True),

                nn.ConvTranspose2d(64 * 2,     64, 4, 2, 1, bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(True),
                nn.ConvTranspose2d(    64,      3, 4, 2, 1, bias=False),
                nn.Sigmoid()
            )


    def forward(self, input):
        return self.main( input )
