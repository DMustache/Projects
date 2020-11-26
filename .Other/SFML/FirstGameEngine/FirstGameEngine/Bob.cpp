#include "Bob.h"

Bob::Bob()
{
	//player Speed
	m_Speed = 400;

	//Connect Textuure with Sprite
	m_Texture.loadFromFile("Bob pic.png");
	m_Sprite.setTexture(m_Texture);

	//Start player position
	m_Position.x = 300;
	m_Position.y = 300;
}

//connect private m_sprite with draw
Sprite Bob::getSprite()
{
	return m_Sprite;
}

void Bob::moveLeft()
{
	m_LeftPressed = true;
}

void Bob::moveRight()
{
	m_RightPressed = true;
}

void Bob::stopLeft()
{
	m_LeftPressed = false;
}

void Bob::stopRight()
{
	m_RightPressed = false;
}
//Player movement per photo
void Bob::update(float elapsedTime)
{
	if (m_RightPressed)
		m_Position.x += m_Speed * elapsedTime;
	if (m_LeftPressed)
		m_Position.x -= m_Speed * elapsedTime;

	//change Sprite Position
	m_Sprite.setPosition(m_Position);
}