[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<br />
<p align="center">
   <img src="https://i.imgur.com/jfyuaOh.png" alt="Logo" width="100"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
   <img src="https://i.imgur.com/4TDD3yS.gif" alt="Cat <3" width="120" height="120">
  <h3 align="center">Emailer</h3>
  <p align="center">
    An awesome bot to send beautiful <strong> Cookie Academy</strong> templates!
    <br />
    <a href="https://github.com/waihankan/emailer"><strong>Explore the docs »</strong></a>
    <br />
    ·
    <a href="https://github.com/waihankan/emailer/issues">Report Bug</a>
    ·
    <a href="https://github.com/waihankan/emailer/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The script is developed for the purpose of sending mass custom html emails. However, we only provide templates for this specific Academy at the moment. Even though we do *not* support the **custom-emailing** version yet, it's possible to send your own custom template with some tweaks. The code still needs some contributions to make a GUI program and automatically fetch data from *Google Sheet*.

### Built With

* [Python 3.8](https://www.python.org/)
* [yagmail](https://github.com/kootenpv/yagmail)
* [keyring](https://pypi.org/project/keyring/)
* [termcolor](https://pypi.org/project/termcolor/)

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

* Python 3.8
  ```sh
  sudo apt-get update
  ```
  ```sh
  sudo apt-get install python 3.8
  ```
  ```sh
  sudo apt-get install python3-pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/waihankan/emailer.git
   ```
2. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage

Here is how to use the code as of latest source code.

1. Go to the folder `hr_html` if you are from **Human Resource Department**, `pr_html` if you are from  **Public Relations Department**, and `academic_html` if you are from **Academic Department**.

2. For **Human Resource Department** 
	 - Firstly, you'll have to fill in the applicants' names and emails using Excel in `hr_applicants.csv` file.
	 - Run `send_email.py` file using the command `python3 send_email.py` and follow the insturctions provided in the program.
	 - The program will show the progress while you're sending custom email to specific recipient. If everything runs smoothly it will show *SUCCESS* , and you are good to leave the program.
	 - Do NOT forget to run the command `python3 clear_csv.py` as soon as you finish your emailing process as it will delete all the *names* and *emails* in `hr_applicants.csv` file.

3. For **Public Relations Department**
	- Firstly, you'll have to fill in the recipients' emails using Excel in `pr_applicants.csv` file.
	- Run `send_pr.py` file using the command `python3 send_pr.py` and follow the insturctions provided in the program.
	- The program will show the progress while you're sending custom email to all the recipients. If everything runs smoothly it will show *Sent Invitation Successfully*, and you are good to leave the program.
	 - Do NOT forget to run the command `python3 clear_csv.py` as soon as you finish your emailing process as it will delete all the *emails* in `pr_applicants.csv` file.

4. For **Academic Deparment**
	- Firstly, you'll have to fill in the applicants' names using Excel in `academic_applicants.csv` file.
	- Add additional attachments in the folder named `attachments`.
	- Run `send_academic.py` file using the command `python3 send_academic.py` and follow the insturctions provided in the program.
	- Last but not least do NOT forget to run the command `python3 clear_csv.py` as soon as you finish your emailing process as it will delete all the *emails* in `academic_applicants.csv` file.

## Demo Images

<p float="left" align="center">
<img src="/assets/cml.gif" /> 

<p float="left" align="center">
  <img src="/assets/interview.png" width="250"/> &nbsp;
  <img src="/assets/event.png" width="250" /> 
</p>

<p float="left" align="center">
  <img src="/assets/discord_invitation.png" width="250" /> &nbsp;   
  <img src="/assets/sorry.png" width="250" />
</p>

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/waihankan/emailer/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contributors
- [@aungbobo04](https://github.com/aungbobo04)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

[@Wai Han](https://twitter.com/WaiHan49607875) - wh.kankan13@gmail.com

Donate Me -> [@Wai Han](https://paypal.me/WaiHanYangon?locale.x=en_US)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Best Readme](https://github.com/othneildrew/Best-README-Template)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/waihankan/emailer.svg?style=for-the-badge
[contributors-url]: https://github.com/waihankan/emailer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/waihankan/emailer.svg?style=for-the-badge
[forks-url]: https://github.com/waihankan/emailer/network/members
[stars-shield]: https://img.shields.io/github/stars/waihankan/emailer.svg?style=for-the-badge
[stars-url]: https://github.com/waihankan/emailer/stargazers
[issues-shield]: https://img.shields.io/github/issues/waihankan/emailer.svg?style=for-the-badge
[issues-url]: https://github.com/waihankan/emailer/issues
[license-shield]: https://img.shields.io/github/license/waihankan/emailer.svg?style=for-the-badge
[license-url]: https://github.com/waihankan/emailer/blob/master/LICENSE
[product-screenshot]: https://i.imgur.com/hY9kal9.jpg
