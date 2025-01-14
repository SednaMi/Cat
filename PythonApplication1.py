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
