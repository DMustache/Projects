#pragma once
#include <SFML/Graphics.hpp>
#include "Bob.h";

using namespace sf;

class Engine
{
private:
	RenderWindow m_Window;

	//BackGround Sprite
	Sprite m_BackgroundSprite;
	Texture m_BackgroundTexture;

	//PreBob
	Bob m_Bob;
	
	void input();
	void update(float dtAsSeconds);
	void draw();

public:
	//Engine Constructer
	Engine();

	//Private Activator
	void start();
};