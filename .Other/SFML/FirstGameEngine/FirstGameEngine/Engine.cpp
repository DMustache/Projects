#include "Engine.h"

Engine::Engine()
{
	//get window resolution and create programm window
	Vector2f resolution;
	resolution.x = VideoMode::getDesktopMode().width;
	resolution.y = VideoMode::getDesktopMode().height;

	m_Window.create(VideoMode(resolution.x, resolution.y), 
		"Simple Game Engine", 
		Style::Fullscreen);

	//Load Background
	m_BackgroundTexture.loadFromFile("backround1920 1200.jpg");

	//Connect sprite with texture
	m_BackgroundSprite.setTexture(m_BackgroundTexture);
}

void Engine::start()
{
	//Time calc
	Clock clock;

	while (m_Window.isOpen())
	{
		//restart timmer and write in dt
		Time dt = clock.restart();

		float dtAsSeconds = dt.asSeconds();

		input();
		update(dtAsSeconds);
		draw();
	}
}