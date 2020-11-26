#include "Engine.h"

void Engine::draw()
{
	//Clear window
	m_Window.clear(Color::White);

	//Phone Draw and Player
	m_Window.draw(m_BackgroundSprite);
	m_Window.draw(m_Bob.getSprite());

	//Write all what include
	m_Window.display();
}