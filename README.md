# Moving Cat Animation

This C# project demonstrates a fun and interactive moving cat animation using Windows Forms. The cat moves around the screen randomly, accompanied by background music, and can also be controlled using keyboard arrow keys.

## Features
- **Random Movements**: The cat moves randomly across the screen.
- **Background Music**: Enjoy looping background music during the animation.
- **Keyboard Interaction**: Move the cat using the arrow keys.

## Requirements
- .NET Framework
- Visual Studio or any C# compiler
- A cat image file
- A background music file (optional)

## Setup
1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    ```

2. **Add your cat image**:
    - Save a cat image to your project's directory (e.g., `path_to_your_cat_image.png`).
    - Replace `"path_to_your_cat_image.png"` in the code with the actual path to your cat image file.

3. **Add your background music file (optional)**:
    - Save a music file to your project's directory (e.g., `path_to_your_background_music.wav`).
    - Replace `"path_to_your_background_music.wav"` in the code with the actual path to your music file.

4. **Compile and run the program**:
    - Open the project in Visual Studio or your preferred C# compiler.
    - Build and run the project to see the cat moving around the screen with background music.

## Code Overview
```csharp
using System;
using System.Drawing;
using System.Media;
using System.Windows.Forms;

public class MovingCatForm : Form
{
    private Timer timer;
    private PictureBox catPictureBox;
    private int catX = 0;
    private int catY = 100;
    private Random random;
    private SoundPlayer soundPlayer;

    public MovingCatForm()
    {
        // Initialize the form
        this.Text = "Moving Cat";
        this.Size = new Size(800, 600);

        // Initialize the picture box for the cat
        catPictureBox = new PictureBox();
        catPictureBox.Image = Image.FromFile("path_to_your_cat_image.png");
        catPictureBox.SizeMode = PictureBoxSizeMode.AutoSize;
        this.Controls.Add(catPictureBox);

        // Initialize the random generator
        random = new Random();

        // Initialize the timer
        timer = new Timer();
        timer.Interval = 100; // 100 milliseconds
        timer.Tick += new EventHandler(UpdateCatPosition);
        timer.Start();

        // Load and play background music
        soundPlayer = new SoundPlayer("path_to_your_background_music.wav");
        soundPlayer.PlayLooping();

        // Key press event
        this.KeyDown += new KeyEventHandler(OnKeyDown);
    }

    private void UpdateCatPosition(object sender, EventArgs e)
    {
        // Randomize the cat's position
        catX += random.Next(-10, 10);
        catY += random.Next(-10, 10);

        // Ensure the cat stays within bounds
        if (catX < 0) catX = 0;
        if (catY < 0) catY = 0;
        if (catX > this.ClientSize.Width - catPictureBox.Width)
            catX = this.ClientSize.Width - catPictureBox.Width;
        if (catY > this.ClientSize.Height - catPictureBox.Height)
            catY = this.ClientSize.Height - catPictureBox.Height;

        catPictureBox.Location = new Point(catX, catY);
    }

    private void OnKeyDown(object sender, KeyEventArgs e)
    {
        // Move cat based on arrow key presses
        switch (e.KeyCode)
        {
            case Keys.Up:
                catY -= 10;
                break;
            case Keys.Down:
                catY += 10;
                break;
            case Keys.Left:
                catX -= 10;
                break;
            case Keys.Right:
                catX += 10;
                break;
        }
        catPictureBox.Location = new Point(catX, catY);
    }

    [STAThread]
    public static void Main()
    {
        Application.Run(new MovingCatForm());
    }
}
