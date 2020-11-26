#pragma once
#include <SFML\Graphics.hpp>

using namespace sf;

class Bob
{
private:
	//Player position
	Vector2f m_Position;

	//New object - Sprite
	Sprite m_Sprite;

	//New texture of object
	Texture m_Texture;
	
	//Player Direction
	bool m_LeftPressed;
	bool m_RightPressed;

	//Player Speed in px per sec
	float m_Speed;

public:
	//Construct player
	Bob();

	//Main function sprite;
	Sprite getSprite();

	//Player Movement;
	void moveLeft();
	
	void moveRight();

	//Player stop;
	void stopLeft();
	
	void stopRight();

	//Every photo func
	void update(float elapsedTime);
};